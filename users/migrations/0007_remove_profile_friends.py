# Generated by Django 2.2.2 on 2019-11-25 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20191029_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
    ]