# Generated by Django 5.1.6 on 2025-03-05 04:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_storage_app', '0019_alter_emailtemplate_subject'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtemplate',
            name='email',
            field=models.EmailField(default='sohamgoswami07@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='emailtemplate',
            unique_together={('user', 'email')},
        ),
    ]
