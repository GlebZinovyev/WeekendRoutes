# Generated by Django 5.0.4 on 2024-04-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sverdlovskroute', '0002_weekend_rout_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='interesting_place',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
