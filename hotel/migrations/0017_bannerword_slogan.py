# Generated by Django 4.0.4 on 2022-07-12 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0016_bannerword'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerword',
            name='slogan',
            field=models.CharField(blank=True, default='s', max_length=300),
        ),
    ]
