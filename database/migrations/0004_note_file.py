# Generated by Django 3.2.2 on 2021-08-14 23:13

import database.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_alter_note_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='file',
            field=models.FileField(default=None, upload_to=database.models.notes_path),
            preserve_default=False,
        ),
    ]