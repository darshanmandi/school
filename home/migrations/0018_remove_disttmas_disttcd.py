# Generated by Django 3.2.9 on 2022-01-20 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_remove_panchayatmas_pancd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disttmas',
            name='disttcd',
        ),
    ]
