# Generated by Django 4.0.1 on 2022-01-31 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_classmas_classlvl'),
    ]

    operations = [
        migrations.CreateModel(
            name='classsubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmm', models.IntegerField()),
                ('pmm', models.IntegerField()),
                ('amm', models.IntegerField()),
                ('subjcombid', models.IntegerField()),
                ('clscd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.classmas')),
                ('subj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subjmas')),
            ],
        ),
    ]
