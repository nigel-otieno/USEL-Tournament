# Generated by Django 5.0.6 on 2024-07-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament_app', '0003_rename_coach_team_coach_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='score_edited',
            field=models.BooleanField(default=False),
        ),
    ]
