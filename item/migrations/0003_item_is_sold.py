# Generated by Django 4.1.5 on 2023-08-01 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_sold',
            field=models.BooleanField(default='False'),
        ),
    ]