Cron job and webhook
====================

If you use `Bambu Cron <https://github.com/iamsteadman/bambu-cron>`_
you can install this cron job (just like any other supported by Bambu Cron) to delete orphaned
attachments. This fires a webhook which you can manage by setting up
`Bambu Webhooks <https://github.com/iamsteadman/bambu-webhooks>`_
to do just about anything you want with it.

Installation
------------

Once you've installed Bambu Attachments, make sure to run ``manage.py cron --setup`` so that Bambu Cron can
pick up the Attachments cron job.