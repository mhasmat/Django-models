# Generated by Django 3.2.2 on 2024-03-26 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0004_wishlist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wishlist',
            options={'verbose_name': 'wish', 'verbose_name_plural': 'wishes'},
        ),
        migrations.AlterModelTable(
            name='wishlist',
            table='e_commerce_wishes',
        ),
    ]