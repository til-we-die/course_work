# Generated by Django 5.1.1 on 2024-12-01 22:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_chatroom_members'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='members',
            field=models.ManyToManyField(related_name='chatrooms', to=settings.AUTH_USER_MODEL),
        ),
    ]
