# Generated by Django 2.0.3 on 2018-03-21 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('type', '0002_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='comboListText',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='summary',
            name='medListText',
            field=models.TextField(default=' '),
        ),
    ]
