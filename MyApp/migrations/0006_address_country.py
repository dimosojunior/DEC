# Generated by Django 4.1 on 2022-10-29 12:40

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0005_coupon_payment_address_order_address_order_coupon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='country',
            field=django_countries.fields.CountryField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]
