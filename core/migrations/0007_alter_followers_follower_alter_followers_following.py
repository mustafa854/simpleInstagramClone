# Generated by Django 4.2.7 on 2023-11-25 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_followers_follower_remove_followers_following_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='core.profile'),
        ),
        migrations.AlterField(
            model_name='followers',
            name='following',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='core.profile'),
        ),
    ]
