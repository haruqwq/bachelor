# Generated by Django 3.2 on 2022-12-17 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0013_card_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='answer_fake1',
        ),
        migrations.RemoveField(
            model_name='card',
            name='answer_fake2',
        ),
    ]