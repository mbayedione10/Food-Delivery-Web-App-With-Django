# Generated by Django 3.1.7 on 2021-03-03 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20210303_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
