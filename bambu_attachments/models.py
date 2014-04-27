from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.conf import settings
from django.template.loader import render_to_string
from bambu_attachments import MIMETYPES, helpers
from mimetypes import guess_type
from os import path

class Attachment(models.Model):
    file = models.FileField(upload_to = helpers.upload_attachment_file)
    size = models.PositiveIntegerField(editable = False)
    """File size (in bytes)"""
    
    mimetype = models.CharField(max_length = 50, editable = False, db_index = True)
    """The file MIME type"""
    
    title = models.CharField(max_length = 100)
    """The attachment title (useful for generating an ``alt`` attribute)"""
    
    description = models.TextField(null = True, blank = True)
    """A full description of the attachment"""
    
    featured = models.BooleanField(default = False, db_index = True)
    """Set to ``True`` when the attachment should be considered that object's featured attachment or
    thumbnail"""
    
    saved = models.BooleanField(default = True, editable = False)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()
    
    def __unicode__(self):
        return self.title
    
    def render(self, *args, **kwargs):
        if not self.mimetype:
            self.mimetype, encoding = guess_type(self.file.name)
        
        if not self.size:
            self.size = path.getsize(settings.MEDIA_ROOT + self.file.name)
        
        ctx = {
            'attachment': self
        }
        
        if not 'nolink' in args:
            ctx['url'] = kwargs.get('link') or self.file.url
        
        if 'align' in kwargs:
            ctx['align'] = kwargs['align']
        
        if self.mimetype in (
            'image/bmp', 'image/x-windows-bmp', 'image/gif',
            'image/jpeg', 'image/pjpeg', 'image/png', 'image/tiff'
        ):
            ctx['size'] = str(kwargs['width'])
            return render_to_string(
                'attachments/image.inc.html',
                ctx
            )
        elif self.mimetype == 'video/mp4':
            ctx['width'] = str(kwargs['width'])
            return render_to_string(
                'attachments/video.inc.html',
                ctx
            )
        else:
            return render_to_string(
                'attachments/download.inc.html',
                ctx
            )
    
    def clean_file(self):
        mimetype, encoding = guess_type(self.file.name)
        if not mimetype in MIMETYPES:
            raise ValidationError('Content type %s not permitted.' % mimetype)
    
    def save(self, *args, **kwargs):
        if self.file and not self.mimetype:
            self.mimetype, encoding = guess_type(self.file.name)
        
        if not self.title:
            self.title = path.splitext(self.file.name)[0]
        
        if not self.size:
            self.size = self.file.size
        
        super(Attachment, self).save(*args, **kwargs)
    
    class Meta:
        unique_together = ('content_type', 'object_id', 'file')
        db_table = 'attachments_attachment'

@receiver(post_delete, sender = Attachment)
def attachment_delete(sender, instance, **kwargs):
    try:
        instance.file.delete(False)
    except:
        pass