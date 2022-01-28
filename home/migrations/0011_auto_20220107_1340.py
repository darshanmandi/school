# Generated by Django 3.2.9 on 2022-01-07 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_staffmas_empcat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffmas',
            name='empcat',
            field=models.CharField(choices=[('T', 'Teaching Staff'), ('N', 'Non Teaching Staff')], default='T', max_length=1),
        ),
        migrations.DeleteModel(
            name='catmas',
        ),
    ]