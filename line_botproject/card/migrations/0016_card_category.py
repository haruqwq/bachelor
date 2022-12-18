# Generated by Django 3.2 on 2022-12-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0015_auto_20221218_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='category',
            field=models.CharField(choices=[('study', '勉強'), ('life', '生活'), ('othre', 'その他')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]