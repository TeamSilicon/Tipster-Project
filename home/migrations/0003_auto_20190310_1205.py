# Generated by Django 2.1.7 on 2019-03-10 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190310_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allgames',
            name='outcome_text',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='allgames',
            name='tip_odd',
            field=models.CharField(default='0.00', max_length=20),
        ),
    ]
