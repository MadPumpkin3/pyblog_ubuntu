# Generated by Django 4.1 on 2024-02-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pycoding',
            name='img_size',
            field=models.IntegerField(max_length=100),
        ),
    ]
