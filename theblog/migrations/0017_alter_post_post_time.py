# Generated by Django 4.0.5 on 2022-09-18 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0016_remove_post_published_date_alter_post_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_time',
            field=models.DateTimeField(blank=True, default=datetime.date.today),
        ),
    ]
