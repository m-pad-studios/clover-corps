# Generated by Django 3.2.23 on 2023-12-14 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_coin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='coin',
            field=models.IntegerField(default=0),
        ),
    ]