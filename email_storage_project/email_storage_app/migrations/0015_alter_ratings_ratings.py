# Generated by Django 5.1.6 on 2025-03-04 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_storage_app', '0014_alter_emailtemplate_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='ratings',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0, null=True),
        ),
    ]
