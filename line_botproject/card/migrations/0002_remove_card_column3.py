# Generated by Django 3.2 on 2022-11-28 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='column3',
        ),
    ]