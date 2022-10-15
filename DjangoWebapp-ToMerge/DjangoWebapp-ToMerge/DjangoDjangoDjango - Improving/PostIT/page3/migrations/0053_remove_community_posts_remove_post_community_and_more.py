# Generated by Django 4.0.6 on 2022-10-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page3', '0052_community_members_community_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='posts',
        ),
        migrations.RemoveField(
            model_name='post',
            name='community',
        ),
        migrations.AddField(
            model_name='community',
            name='post',
            field=models.ManyToManyField(blank=True, default=None, related_name='community_posts', to='page3.post'),
        ),
    ]
