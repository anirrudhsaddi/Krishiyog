# Generated by Django 2.0.1 on 2018-01-29 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krishiyog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='farm_name',
            field=models.CharField(default='first', max_length=30),
        ),
    ]
