# Generated by Django 3.1.6 on 2021-04-02 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0002_auto_20210318_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='cart_id',
        ),
    ]
