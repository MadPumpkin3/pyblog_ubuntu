# Generated by Django 4.1 on 2024-02-23 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0007_alter_pycoding_img_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pycoding',
            name='img_size',
            field=models.IntegerField(choices=[(70, '70%'), (30, '30%'), (40, '40%'), (100, '100%'), (50, '50%')]),
        ),
    ]
