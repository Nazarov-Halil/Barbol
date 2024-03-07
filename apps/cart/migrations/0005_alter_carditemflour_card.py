# Generated by Django 5.0.2 on 2024-03-05 09:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_carditemflour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carditemflour',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flours_items', to='cart.card', verbose_name='Карзина'),
        ),
    ]