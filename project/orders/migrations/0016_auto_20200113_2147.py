# Generated by Django 2.2.7 on 2020-01-13 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_revision_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='order_stage',
            field=models.CharField(choices=[('Design pending approval', 'Design pending approval'), ('Revisions requested', 'Revisions requested'), ('Design accepted', 'Design accepted')], default='Design pending approval', max_length=120),
        ),
    ]