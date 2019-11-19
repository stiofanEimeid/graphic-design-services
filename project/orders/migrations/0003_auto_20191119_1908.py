# Generated by Django 2.2.7 on 2019-11-19 19:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20191119_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='time_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.CharField(choices=[('Logo', 'Logo'), ('Icon', 'Icon'), ('Poster', 'Poster'), ('Website', 'Website')], default='Logo', max_length=120),
        ),
    ]
