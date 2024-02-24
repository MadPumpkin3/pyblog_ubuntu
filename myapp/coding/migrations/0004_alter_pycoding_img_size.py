# Generated by Django 4.1 on 2024-02-24 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0003_alter_pycoding_img_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pycoding',
            name='img_size',
            field=models.IntegerField(choices=[(30, '30%'), (70, '70%'), (50, '50%'), (40, '40%'), (100, '100%')]),
        ),
    ]