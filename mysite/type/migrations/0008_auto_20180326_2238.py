# Generated by Django 2.0.3 on 2018-03-27 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('type', '0007_applyingas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyingas',
            name='choice',
            field=models.CharField(choices=[("Zachary's Live Test", "Zachary's Live Test"), ('Zachary Nowak', 'Zachary Nowak'), ('A final test hopefully', 'A final test hopefully'), ('Last Test', 'Last Test'), ('The Homogay Communist', 'The Homogay Communist'), ('Litzy', 'Litzy'), ('Meredith', 'Meredith'), ('Cassandra', 'Cassandra'), ("Let's try this again", "Let's try this again"), ('Alexandria Camposs-Preierez-Shalvez', 'Alexandria Camposs-Preierez-Shalvez'), ('Alexandria Camposs-Preierez-Shalvez', 'Alexandria Camposs-Preierez-Shalvez'), ('Alexandria Camposs-Preierez-Shalvez', 'Alexandria Camposs-Preierez-Shalvez'), ('This is meredith again.', 'This is meredith again.')], max_length=100),
        ),
    ]
