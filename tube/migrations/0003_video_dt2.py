# Generated by Django 3.1.7 on 2021-04-17 08:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0002_video_edited'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='dt2',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='最終更新日'),
        ),
    ]
