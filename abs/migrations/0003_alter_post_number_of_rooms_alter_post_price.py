# Generated by Django 5.0 on 2023-12-11 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abs', '0002_post_number_of_rooms_post_price_post_type_of_housing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='number_of_rooms',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
