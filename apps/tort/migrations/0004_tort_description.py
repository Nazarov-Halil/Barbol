# Generated by Django 5.0.2 on 2024-02-27 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tort', '0003_rename_image_tort_tort_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tort',
            name='description',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
