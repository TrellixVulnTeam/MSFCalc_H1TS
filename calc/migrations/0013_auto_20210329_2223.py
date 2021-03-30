# Generated by Django 3.1.3 on 2021-03-29 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0012_auto_20210326_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supply',
            name='packaging_size',
            field=models.IntegerField(blank=True, null=True, verbose_name='Packaging'),
        ),
        migrations.AlterField(
            model_name='supply',
            name='supply_strength',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Supply Strength'),
        ),
    ]
