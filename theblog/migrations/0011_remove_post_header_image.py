# Generated by Django 4.0.5 on 2022-09-17 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0010_post_header_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='header_image',
        ),
    ]
