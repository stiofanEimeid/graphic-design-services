# Generated by Django 2.2.7 on 2020-01-30 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20200130_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='design',
            old_name='final_design',
            new_name='sub_design',
        ),
    ]
