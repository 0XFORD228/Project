# Generated by Django 4.2.3 on 2023-08-11 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Назва')),
                ('anons', models.CharField(max_length=260, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Стаття')),
                ('date', models.TimeField(verbose_name='Дата Публікації')),
            ],
        ),
    ]
