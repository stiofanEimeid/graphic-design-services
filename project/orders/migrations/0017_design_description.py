# Generated by Django 2.2.7 on 2020-01-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20200113_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='description',
            field=models.TextField(default='N/A'),
            preserve_default=False,
        ),
    ]
