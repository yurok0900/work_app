# Generated by Django 3.2 on 2021-05-05 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20210505_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmodel',
            name='text',
        ),
    ]
