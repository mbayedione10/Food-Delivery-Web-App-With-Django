# Generated by Django 3.1.7 on 2021-03-03 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20210303_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
