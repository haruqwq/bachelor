# Generated by Django 3.2 on 2022-12-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0016_card_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='category',
            field=models.CharField(choices=[('study', '勉強'), ('programming', 'プログラミング'), ('othre', 'その他')], max_length=100),
        ),
    ]