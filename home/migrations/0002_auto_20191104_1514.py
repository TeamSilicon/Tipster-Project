# Generated by Django 2.2.4 on 2019-11-04 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allgames',
            old_name='ft_results',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='allgames',
            old_name='tip_odd',
            new_name='odds',
        ),
        migrations.RenameField(
            model_name='allgames',
            old_name='tip',
            new_name='pick',
        ),
        migrations.RenameField(
            model_name='allgames',
            old_name='match_date',
            new_name='result',
        ),
        migrations.RenameField(
            model_name='allgames',
            old_name='outcome_text',
            new_name='start_time',
        ),
        migrations.RenameField(
            model_name='allgames',
            old_name='time',
            new_name='won_or_lost',
        ),
        migrations.RenameField(
            model_name='featured',
            old_name='ft_results',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='featured',
            old_name='tip_odd',
            new_name='odds',
        ),
        migrations.RenameField(
            model_name='featured',
            old_name='tip',
            new_name='pick',
        ),
        migrations.RenameField(
            model_name='featured',
            old_name='match_date',
            new_name='result',
        ),
        migrations.RenameField(
            model_name='featured',
            old_name='outcome_text',
            new_name='start_time',
        ),
        migrations.RenameField(
            model_name='featured',
            old_name='time',
            new_name='won_or_lost',
        ),
        migrations.RenameField(
            model_name='over15',
            old_name='ft_results',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='over15',
            old_name='match_date',
            new_name='result',
        ),
        migrations.RenameField(
            model_name='over15',
            old_name='outcome_text',
            new_name='start_time',
        ),
        migrations.RenameField(
            model_name='over15',
            old_name='time',
            new_name='won_or_lost',
        ),
        migrations.RenameField(
            model_name='over25',
            old_name='ft_results',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='over25',
            old_name='match_date',
            new_name='result',
        ),
        migrations.RenameField(
            model_name='over25',
            old_name='outcome_text',
            new_name='start_time',
        ),
        migrations.RenameField(
            model_name='over25',
            old_name='time',
            new_name='won_or_lost',
        ),
        migrations.RenameField(
            model_name='over35',
            old_name='ft_results',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='over35',
            old_name='match_date',
            new_name='result',
        ),
        migrations.RenameField(
            model_name='over35',
            old_name='outcome_text',
            new_name='start_time',
        ),
        migrations.RenameField(
            model_name='over35',
            old_name='time',
            new_name='won_or_lost',
        ),
        migrations.RenameField(
            model_name='tipgg',
            old_name='ft_results',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='tipgg',
            old_name='match_date',
            new_name='result',
        ),
        migrations.RenameField(
            model_name='tipgg',
            old_name='outcome_text',
            new_name='start_time',
        ),
        migrations.RenameField(
            model_name='tipgg',
            old_name='time',
            new_name='won_or_lost',
        ),
    ]
