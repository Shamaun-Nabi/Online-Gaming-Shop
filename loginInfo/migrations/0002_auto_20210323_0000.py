# Generated by Django 3.1.6 on 2021-03-22 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginInfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
