# Generated by Django 4.0.4 on 2022-04-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_alter_booking_order_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='no_day',
            field=models.IntegerField(default=1),
        ),
    ]
