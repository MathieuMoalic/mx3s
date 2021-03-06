# Generated by Django 3.1.7 on 2021-02-27 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Gpu',
            fields=[(
                'id',
                models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID',
                ),
            )],
        ),
        migrations.CreateModel(
            name='Simulation',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=200)),
                ('start_time',
                 models.DateTimeField(verbose_name='time started')),
                ('end_time', models.DateTimeField(verbose_name='time ended')),
                ('duration', models.DurationField()),
                ('queued', models.BooleanField()),
                ('running', models.BooleanField()),
                ('finished', models.BooleanField(default=False)),
                ('port', models.PositiveIntegerField()),
                (
                    'path',
                    models.FilePathField(
                        path='/mnt/g/Mathieu/simulations/server'),
                ),
                (
                    'current_gpu',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='server.gpu',
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name='gpu',
            name='current_simulation',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='server.simulation',
            ),
        ),
    ]
