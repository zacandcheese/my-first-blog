# Generated by Django 2.0.3 on 2018-03-27 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('type', '0006_applying'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyingAs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('Zachary Nowak', 'Zachary Nowak'), ('Matthew Nowak', 'Matthew Nowak'), ('Haley Nowak', 'Haley Nowak')], max_length=3)),
            ],
        ),
    ]
