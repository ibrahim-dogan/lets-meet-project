# Generated by Django 2.1.4 on 2018-12-13 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pics/default.png', upload_to='profile_pics'),
        ),
    ]
