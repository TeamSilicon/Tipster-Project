# Generated by Django 2.2.4 on 2019-11-04 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20191104_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='over15',
            old_name='tip_ov_odd',
            new_name='tip_ov_odds',
        ),
        migrations.RenameField(
            model_name='over25',
            old_name='tip_ov_odd',
            new_name='tip_ov_odds',
        ),
        migrations.RenameField(
            model_name='over35',
            old_name='tip_ov_odd',
            new_name='tip_ov_odds',
        ),
        migrations.RenameField(
            model_name='tipgg',
            old_name='tip_gg_odd',
            new_name='tip_gg_odds',
        ),
    ]
