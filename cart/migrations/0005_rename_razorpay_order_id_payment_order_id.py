# Generated by Django 5.1.2 on 2024-11-20 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_rename_order_id_payment_razorpay_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='razorpay_order_id',
            new_name='order_id',
        ),
    ]
