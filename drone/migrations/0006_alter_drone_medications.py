# Generated by Django 4.0.3 on 2022-10-07 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone', '0005_alter_medication_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='medications',
            field=models.ManyToManyField(blank=True, null=True, to='drone.medication'),
        ),
    ]
