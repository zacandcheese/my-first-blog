# Generated by Django 2.0.3 on 2018-03-31 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('type', '0008_auto_20180326_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyingas',
            name='choice',
            field=models.CharField(max_length=100),
        ),
    ]
