# Generated by Django 4.0.2 on 2022-02-28 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_listing_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='user',
        ),
    ]
