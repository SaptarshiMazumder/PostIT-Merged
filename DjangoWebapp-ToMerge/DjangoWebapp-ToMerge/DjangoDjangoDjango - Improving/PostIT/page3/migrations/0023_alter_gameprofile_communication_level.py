# Generated by Django 4.0.6 on 2022-12-13 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page3', '0022_remove_gameprofile_free_time_slots_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameprofile',
            name='communication_level',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
