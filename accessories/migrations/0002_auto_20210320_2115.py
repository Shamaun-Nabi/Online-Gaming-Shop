# Generated by Django 3.1.6 on 2021-03-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessories',
            name='price',
            field=models.FloatField(default=500),
        ),
        migrations.AlterField(
            model_name='accessories',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
