# Generated by Django 3.2.9 on 2022-01-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20220112_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffmas',
            name='empcat',
        ),
        migrations.AddField(
            model_name='desigmas',
            name='desgcat',
            field=models.CharField(choices=[('T', 'Teaching Staff'), ('N', 'Non Teaching Staff'), ('S', 'SMC')], default='T', max_length=1),
        ),
    ]
