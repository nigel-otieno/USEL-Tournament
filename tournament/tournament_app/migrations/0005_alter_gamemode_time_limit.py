# Generated by Django 5.0.6 on 2024-06-06 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament_app', '0004_gamemode_tournament_game_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemode',
            name='time_limit',
            field=models.DurationField(blank=True, null=True),
        ),
    ]