# Generated by Django 5.1.4 on 2024-12-20 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_menu_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dish',
            table='menu_dish',
        ),
        migrations.AlterModelTable(
            name='menu',
            table='menu_menu',
        ),
    ]
