# Generated by Django 3.2.3 on 2021-05-31 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0006_rename_video_image_url_workouts_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workouts',
            name='image_url',
        ),
    ]
