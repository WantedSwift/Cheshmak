# Generated by Django 4.0 on 2022-12-13 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_main_chat_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='main_chat1',
        ),
    ]
