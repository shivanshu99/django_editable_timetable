# Generated by Django 3.0.5 on 2020-07-26 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_auto_20200726_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='esub3',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
