# Generated by Django 5.1.6 on 2025-03-04 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_storage_app', '0010_remove_emailtemplate_rating_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtemplate',
            name='rating',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default='0', null=True),
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
    ]
