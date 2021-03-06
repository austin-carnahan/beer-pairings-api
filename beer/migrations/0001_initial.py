# Generated by Django 2.2.5 on 2019-09-30 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('abv', models.FloatField(blank=True, null=True)),
                ('ibu', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(blank=True, max_length=80)),
                ('address2', models.CharField(blank=True, max_length=80)),
                ('address3', models.CharField(blank=True, max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('state', models.CharField(blank=True, max_length=80)),
                ('zipcode', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(max_length=80)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic', models.CharField(max_length=60)),
                ('detailed', models.CharField(blank=True, max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Pairing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('approved', models.BooleanField(default=False)),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.Beer')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Brewery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.Location')),
            ],
        ),
        migrations.AddField(
            model_name='beer',
            name='brewery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.Brewery'),
        ),
        migrations.AddField(
            model_name='beer',
            name='sighting',
            field=models.ManyToManyField(related_name='sightings', to='beer.Location'),
        ),
        migrations.AddField(
            model_name='beer',
            name='style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.Style'),
        ),
        migrations.AddField(
            model_name='beer',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='beer.Tag'),
        ),
    ]
