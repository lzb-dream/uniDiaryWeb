# Generated by Django 4.1.2 on 2022-10-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apidiary', '0003_alter_user_headportrait'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='headPortrait',
            field=models.CharField(blank=True, default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='updateTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]