# Generated by Django 2.1.4 on 2018-12-10 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='biletix_url',
            new_name='url',
        ),
    ]
