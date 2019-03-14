# Generated by Django 2.1.7 on 2019-03-13 06:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20190313_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата обновления статьи'),
        ),
    ]