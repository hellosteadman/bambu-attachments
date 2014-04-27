from bambu_cron import CronJob, site, DAY
from django.conf import settings
from bambu_attachments.models import Attachment
from os import remove, path, listdir

ROOT = path.join(settings.MEDIA_ROOT, 'attachments')

class AttachmentClearoutJob(CronJob):
    """Clears up orphaned attachments every day"""
    
    frequency = DAY
    
    def run(self, logger):
        files = []
        for a in Attachment.objects.all():
            files.append(a.file.path)
            if a.content_object is None:
                a.delete()
        
        for p in [p for p in listdir(ROOT) if path.isdir(path.join(ROOT, p))]:
            if p.startswith('.'):
                continue
            
            for pp in [pp for pp in listdir(path.join(ROOT, p)) if path.isdir(path.join(ROOT, p, pp))]:
                if pp.startswith('.'):
                    continue

                for f in listdir(path.join(ROOT, p, pp)):
                    if f.startswith('.'):
                        continue
                    
                    ff = path.join(ROOT, p, pp, f)
                    if not ff in files:
                        remove(ff)

site.register(AttachmentClearoutJob)