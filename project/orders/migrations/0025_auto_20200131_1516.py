# Generated by Django 2.2.7 on 2020-01-31 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20200131_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='design_number',
            new_name='design_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='reference',
        ),
    ]
