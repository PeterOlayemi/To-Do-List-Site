# Generated by Django 4.0.6 on 2022-09-07 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0015_rename_mark_as_done_todo_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
