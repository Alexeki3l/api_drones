# Generated by Django 4.0.3 on 2022-10-07 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone', '0012_drone_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='state',
            field=models.CharField(blank=True, choices=[('1', 'IDLE'), ('2', 'LOADING'), ('3', 'LOADED'), ('4', 'DELIVERING'), ('5', 'DELIVERED'), ('6', 'RETURNING')], max_length=1, null=True),
        ),
    ]
