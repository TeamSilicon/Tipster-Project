# Generated by Django 2.1.5 on 2019-01-31 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZuluBet',
            fields=[
                ('match_date', models.CharField(max_length=40)),
                ('time', models.CharField(max_length=40)),
                ('teams', models.CharField(max_length=400, primary_key=True, serialize=False)),
                ('tip', models.CharField(max_length=40)),
                ('tip_odd', models.CharField(max_length=20)),
                ('ft_results', models.CharField(max_length=40)),
            ],
        ),
    ]