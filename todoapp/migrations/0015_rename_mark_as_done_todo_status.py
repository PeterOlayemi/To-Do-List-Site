# Generated by Django 4.0.6 on 2022-08-30 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0014_alter_todo_mark_as_done'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='mark_as_done',
            new_name='status',
        ),
    ]
