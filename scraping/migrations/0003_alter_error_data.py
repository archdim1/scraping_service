# Generated by Django 3.2.7 on 2021-09-24 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_error'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='data',
            field=models.JSONField(),
        ),
    ]
