# Generated by Django 4.2.3 on 2023-08-15 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_1', '0002_forum_publications_alter_publications_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum_publications',
            name='anons',
        ),
        migrations.RemoveField(
            model_name='publications',
            name='anons',
        ),
    ]
