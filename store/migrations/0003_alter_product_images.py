# Generated by Django 5.0.4 on 2024-04-30 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.CharField(max_length=200),
        ),
    ]
