# Generated by Django 4.2 on 2024-03-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_cartdetail_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cartdetail',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
