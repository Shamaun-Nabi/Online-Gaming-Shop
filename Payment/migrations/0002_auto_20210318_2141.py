# Generated by Django 3.1.7 on 2021-03-18 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
        ('Payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='cart_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Cart.cart'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
