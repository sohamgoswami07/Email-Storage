# Generated by Django 5.1.6 on 2025-02-24 14:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_storage_app', '0002_rename_images_emailtemplate_attachments'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtemplate',
            name='user',
            field=models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default='True',
        ),
    ]
