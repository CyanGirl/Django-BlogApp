# Generated by Django 3.2.4 on 2021-06-20 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(upload_to='blog_images'),
        ),
    ]
