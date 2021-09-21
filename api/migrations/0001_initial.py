# Generated by Django 3.2.4 on 2021-09-21 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('language', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('total_seats', models.IntegerField(default=100)),
                ('available_seats', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.city')),
            ],
        ),
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.city')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.movie')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.show')),
                ('theatre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.theatre')),
            ],
        ),
    ]