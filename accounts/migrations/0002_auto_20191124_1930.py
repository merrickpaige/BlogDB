# Generated by Django 2.2.2 on 2019-11-25 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequest',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='friendrequest',
            name='to_user',
        ),
        migrations.DeleteModel(
            name='FProfile',
        ),
        migrations.DeleteModel(
            name='FriendRequest',
        ),
    ]