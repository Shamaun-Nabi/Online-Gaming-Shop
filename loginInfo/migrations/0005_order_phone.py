# Generated by Django 3.1.6 on 2021-04-05 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginInfo', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=14),
        ),
    ]
