# Generated by Django 4.0.3 on 2022-05-18 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_rename_subscribers_subscribe'),
    ]

    operations = [
        migrations.DeleteModel(
            name='subscribe',
        ),
    ]