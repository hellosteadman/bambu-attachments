from django.contrib.contenttypes import generic
from bambu_attachments.models import Attachment
from bambu_attachments.forms import AttachmentForm

class AttachmentInline(generic.GenericStackedInline):
    model = Attachment
    extra = 0
    form = AttachmentForm