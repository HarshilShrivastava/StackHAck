# Generated by Django 3.0.6 on 2020-05-26 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200526_0807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='name',
            new_name='Priority',
        ),
    ]