# Generated by Django 4.0.6 on 2022-12-01 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page3', '0012_alter_gameprofile_additional_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='none', max_length=50, null=True),
        ),
    ]