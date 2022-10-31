# Generated by Django 4.1.2 on 2022-10-15 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diary', models.TextField()),
                ('writeTime', models.DateTimeField()),
                ('mood', models.CharField(max_length=10)),
                ('weather', models.CharField(max_length=10)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('thumbUpNumber', models.IntegerField(default=0)),
                ('flowerCount', models.IntegerField(default=0)),
                ('squareSwitch', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '用户日记',
                'verbose_name_plural': '用户日记',
                'db_table': 'diary',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('openId', models.CharField(max_length=255)),
                ('addTime', models.DateTimeField(blank=True, max_length=255)),
                ('updateTime', models.DateTimeField(blank=True)),
                ('headPortrait', models.CharField(blank=True, max_length=255)),
                ('state', models.BooleanField(default=True)),
                ('flowers', models.IntegerField(default=0)),
                ('money', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('diaryNumber', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.CharField(max_length=255)),
                ('diary', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apidiary.diary')),
            ],
            options={
                'verbose_name': '用户视频',
                'verbose_name_plural': '用户视频',
                'db_table': 'video',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.CharField(max_length=255)),
                ('diary', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apidiary.diary')),
            ],
            options={
                'verbose_name': '日记图片',
                'verbose_name_plural': '日记图片',
                'db_table': 'image',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='diary',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_openid', to='apidiary.user'),
        ),
    ]