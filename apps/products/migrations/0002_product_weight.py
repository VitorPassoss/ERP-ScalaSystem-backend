# Generated by Django 4.0 on 2023-06-23 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=21, null=True),
        ),
    ]
