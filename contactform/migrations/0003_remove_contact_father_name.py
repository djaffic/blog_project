# Generated by Django 2.1.7 on 2019-03-29 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactform', '0002_auto_20190328_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='father_name',
        ),
    ]
