# Generated by Django 2.2.7 on 2020-01-12 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_design_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='revision',
            name='type',
            field=models.CharField(default='Logo', max_length=120),
            preserve_default=False,
        ),
    ]