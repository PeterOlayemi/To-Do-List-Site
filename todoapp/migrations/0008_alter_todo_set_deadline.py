# Generated by Django 4.0.6 on 2022-08-30 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0007_alter_todo_set_deadline_alter_todo_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='set_deadline',
            field=models.DateField(),
        ),
    ]