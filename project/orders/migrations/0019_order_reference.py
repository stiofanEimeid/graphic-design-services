# Generated by Django 2.2.7 on 2020-01-30 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='reference',
            field=models.FileField(blank=True, null=True, upload_to='references'),
        ),
    ]
