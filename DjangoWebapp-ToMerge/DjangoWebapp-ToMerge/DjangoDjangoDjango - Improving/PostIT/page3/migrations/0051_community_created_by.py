# Generated by Django 4.0.6 on 2022-10-15 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('page3', '0050_remove_community_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='created_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
