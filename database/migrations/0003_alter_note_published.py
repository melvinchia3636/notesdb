# Generated by Django 3.2.2 on 2021-08-14 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_rename_notes_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='published',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]