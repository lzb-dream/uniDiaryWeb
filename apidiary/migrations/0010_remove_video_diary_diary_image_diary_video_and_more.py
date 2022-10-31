# Generated by Django 4.1.2 on 2022-10-31 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apidiary', '0009_image_addtime_video_addtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='diary',
        ),
        migrations.AddField(
            model_name='diary',
            name='image',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='diary',
            name='video',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
