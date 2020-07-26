# Generated by Django 3.0.5 on 2020-07-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_auto_20200726_1400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='edays',
            new_name='eid',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='esub1',
            new_name='ename',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='esub2',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='esub3',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='esub4',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='esub5',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='esub6',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='esub7',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='esub8',
        ),
        migrations.AddField(
            model_name='employee',
            name='econtact',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='eemail',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]