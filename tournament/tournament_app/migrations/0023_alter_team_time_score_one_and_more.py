# Generated by Django 5.0.6 on 2024-06-26 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament_app', '0022_tournament_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='time_score_one',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='time_score_three',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='time_score_two',
            field=models.DurationField(blank=True, null=True),
        ),
    ]