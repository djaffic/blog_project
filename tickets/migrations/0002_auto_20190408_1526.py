# Generated by Django 2.1.7 on 2019-04-08 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='room',
            field=models.PositiveIntegerField(verbose_name='Кабинет'),
        ),
    ]
