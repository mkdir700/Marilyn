# Generated by Django 3.0.3 on 2020-06-10 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0003_auto_20200610_0928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attachmentmodel',
            old_name='cid',
            new_name='content',
        ),
    ]
