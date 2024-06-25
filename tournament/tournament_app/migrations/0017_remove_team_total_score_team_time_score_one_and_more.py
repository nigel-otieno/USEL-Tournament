# Generated by Django 5.0.6 on 2024-06-25 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament_app', '0016_tournament_rules'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='total_score',
        ),
        migrations.AddField(
            model_name='team',
            name='time_score_one',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='time_score_three',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='time_score_two',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='coach',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]