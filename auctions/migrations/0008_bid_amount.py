# Generated by Django 4.0.2 on 2022-02-27 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_remove_bid_amount_remove_bid_listing_bid_bids_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=11, null=True),
        ),
    ]
