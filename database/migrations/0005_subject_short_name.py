# Generated by Django 3.2.2 on 2021-08-17 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_note_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='short_name',
            field=models.CharField(default='NICE', max_length=16),
            preserve_default=False,
        ),
    ]