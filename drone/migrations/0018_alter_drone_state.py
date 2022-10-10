# Generated by Django 4.0.3 on 2022-10-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone', '0017_dronehistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='state',
            field=models.CharField(blank=True, choices=[('1', 'IDLE'), ('2', 'LOADING'), ('3', 'LOADED'), ('4', 'DELIVERING'), ('5', 'DELIVERED'), ('6', 'RETURNING'), ('6', 'RETURNING')], max_length=1),
        ),
    ]
