# Generated by Django 2.1.5 on 2020-05-22 09:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20190403_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='date_of_birth',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]