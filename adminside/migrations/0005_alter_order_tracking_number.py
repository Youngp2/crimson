# Generated by Django 5.0.6 on 2024-08-30 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0004_order_arrival_time_alter_order_tracking_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(default='EXWA4dece28e-18d7-44c8-ORDER', max_length=30, unique=True),
        ),
    ]
