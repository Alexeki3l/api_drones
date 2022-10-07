# Generated by Django 4.0.3 on 2022-10-06 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone', '0002_remove_medication_drone_drone_medications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='model',
            field=models.CharField(choices=[('1', 'Lightweigth'), ('2', 'Middleweigth'), ('3', 'Cruiserweigth'), ('4', 'Heavyweigth')], max_length=15),
        ),
        migrations.AlterField(
            model_name='drone',
            name='state',
            field=models.CharField(choices=[('1', 'IDLE'), ('2', 'LOADING'), ('3', 'LOADED'), ('4', 'DELIVERING'), ('5', 'DELIVERED'), ('6', 'RETURNING')], max_length=10),
        ),
    ]
