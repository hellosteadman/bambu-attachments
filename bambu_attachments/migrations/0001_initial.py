# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import bambu_attachments.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=bambu_attachments.helpers.upload_attachment_file)),
                ('size', models.PositiveIntegerField(editable=False)),
                ('mimetype', models.CharField(max_length=50, editable=False, db_index=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
                ('featured', models.BooleanField(default=False, db_index=True)),
                ('saved', models.BooleanField(default=True, editable=False)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'attachments_attachment',
            },
        ),
        migrations.AlterUniqueTogether(
            name='attachment',
            unique_together=set([('content_type', 'object_id', 'file')]),
        ),
    ]
