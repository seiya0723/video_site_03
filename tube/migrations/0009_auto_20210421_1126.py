# Generated by Django 3.1.2 on 2021-04-21 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0008_delete_videoedited'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(blank=True, upload_to='tube/image/', verbose_name='画像'),
        ),
        migrations.AddField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, upload_to='tube/video/', verbose_name='動画'),
        ),
    ]