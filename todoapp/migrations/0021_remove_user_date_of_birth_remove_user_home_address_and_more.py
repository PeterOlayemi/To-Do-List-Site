# Generated by Django 4.1.4 on 2023-03-06 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0020_alter_todo_short_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='home_address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state_of_origin',
        ),
    ]
