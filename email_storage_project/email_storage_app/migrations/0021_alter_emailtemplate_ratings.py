# Generated by Django 5.1.6 on 2025-03-05 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_storage_app', '0020_emailtemplate_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailtemplate',
            name='ratings',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0, null=True),
        ),
    ]
