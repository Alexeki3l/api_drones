# Generated by Django 4.0.3 on 2022-10-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone', '0018_alter_drone_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='image',
            field=models.ImageField(blank=True, upload_to='medication'),
        ),
    ]
