# Generated by Django 5.0.2 on 2024-03-05 05:24

import utils.image_path
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('tort_image', models.ImageField(blank=True, null=True, upload_to=utils.image_path.upload_products, verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Торт',
                'verbose_name_plural': 'Торты',
            },
        ),
    ]
