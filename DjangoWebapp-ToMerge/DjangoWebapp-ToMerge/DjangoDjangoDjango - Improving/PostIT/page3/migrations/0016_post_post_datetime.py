# Generated by Django 4.0.6 on 2022-08-17 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('page3', '0015_post_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
