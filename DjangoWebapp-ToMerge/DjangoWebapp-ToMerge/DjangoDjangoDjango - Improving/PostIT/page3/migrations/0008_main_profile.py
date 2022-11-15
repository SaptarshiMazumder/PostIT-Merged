# Generated by Django 4.0.6 on 2022-11-15 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('page3', '0007_gameprofile_is_main_gamer_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_gamer_profile', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='page3.gameprofile')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
