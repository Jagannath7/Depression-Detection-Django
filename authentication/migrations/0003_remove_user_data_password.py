# Generated by Django 3.1.4 on 2020-12-26 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20201226_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='password',
        ),
    ]
