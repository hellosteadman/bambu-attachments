from django.db import models
from django.contrib.contenttypes import generic
from bambu_attachments.models import Attachment

class Item(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    attachments = generic.GenericRelation(Attachment)
    
    def __unicode__(self):
        return self.name