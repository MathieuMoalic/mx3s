# Generated by Django 3.1.7 on 2021-03-15 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0016_simulation_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gpu',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='simulation',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='simulation',
            name='name',
        ),
        migrations.RemoveField(
            model_name='simulation',
            name='path',
        ),
        migrations.RemoveField(
            model_name='simulation',
            name='port',
        ),
    ]