# Generated by Django 3.0.1 on 2019-12-27 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0004_auto_20191227_2137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='trailer',
            new_name='trailer_youtube_id',
        ),
    ]
