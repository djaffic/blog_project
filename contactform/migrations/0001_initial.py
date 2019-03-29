# Generated by Django 2.1.7 on 2019-03-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('father_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('content', models.TextField(verbose_name='Текст обращения')),
            ],
            options={
                'verbose_name': 'Контакная форма',
                'verbose_name_plural': 'Контакные формы',
                'ordering': ['-last_name'],
            },
        ),
    ]
