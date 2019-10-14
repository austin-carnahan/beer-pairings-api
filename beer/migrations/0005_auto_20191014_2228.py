# Generated by Django 2.2.5 on 2019-10-14 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0004_auto_20191014_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='pairings',
            field=models.ManyToManyField(blank=True, through='beer.Pairing', to='beer.Food'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='sighting',
            field=models.ManyToManyField(blank=True, related_name='sightings', to='beer.Location'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='tags',
            field=models.ManyToManyField(blank=True, to='beer.Tag'),
        ),
    ]
