# Generated by Django 2.2.4 on 2019-08-16 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20190816_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menus',
            name='number',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
    ]