# Generated by Django 5.0.6 on 2024-06-24 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament_app', '0011_alter_tournament_game_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='game_mode',
            field=models.CharField(choices=[('TimeAttack', 'Time Attack'), ('HighestScore', 'Highest Score')], default='TimeAttack', max_length=20),
        ),
    ]