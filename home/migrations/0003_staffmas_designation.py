# Generated by Django 3.2.9 on 2022-01-05 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_desigmas'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffmas',
            name='designation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.desigmas'),
        ),
    ]
