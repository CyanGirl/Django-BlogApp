# Generated by Django 3.2.4 on 2021-07-05 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210630_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.CharField(default='Anonymous', max_length=20),
        ),
    ]
