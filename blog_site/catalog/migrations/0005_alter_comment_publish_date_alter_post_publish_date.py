# Generated by Django 4.1.1 on 2022-09-29 09:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_comment_options_comment_publish_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 29, 12, 31, 46, 6341), verbose_name='pubdate'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 29, 12, 31, 46, 5343), verbose_name='pubdate'),
        ),
    ]