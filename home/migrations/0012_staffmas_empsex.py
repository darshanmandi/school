# Generated by Django 3.2.9 on 2022-01-07 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20220107_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffmas',
            name='empsex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Feamle'), ('O', 'Other')], default='M', max_length=1),
        ),
    ]
