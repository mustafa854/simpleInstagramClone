# Generated by Django 4.2.7 on 2023-11-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followers',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='followers',
            name='following',
        ),
        migrations.AddField(
            model_name='followers',
            name='follower',
            field=models.ManyToManyField(related_name='follower', to='core.profile'),
        ),
        migrations.AddField(
            model_name='followers',
            name='following',
            field=models.ManyToManyField(related_name='following', to='core.profile'),
        ),
    ]
