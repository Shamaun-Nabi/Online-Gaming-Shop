# Generated by Django 3.1.7 on 2021-03-17 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('name', models.CharField(max_length=15)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]