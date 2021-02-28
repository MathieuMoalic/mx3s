# Generated by Django 3.1.7 on 2021-02-28 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20210228_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpu',
            name='current_simulation',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.simulation'),
        ),
        migrations.AlterField(
            model_name='simulation',
            name='current_gpu',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.gpu'),
        ),
        migrations.AlterField(
            model_name='simulation',
            name='duration',
            field=models.DurationField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='simulation',
            name='end_time',
            field=models.DateTimeField(blank=True, default=None, verbose_name='time ended'),
        ),
        migrations.AlterField(
            model_name='simulation',
            name='port',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='simulation',
            name='start_time',
            field=models.DateTimeField(blank=True, default=None, verbose_name='time started'),
        ),
    ]
