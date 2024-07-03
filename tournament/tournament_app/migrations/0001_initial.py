# Generated by Django 5.0.6 on 2024-07-03 22:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('emergency_contact_first_name', models.CharField(max_length=100)),
                ('emergency_contact_last_name', models.CharField(max_length=100)),
                ('emergency_contact_phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100)),
                ('state_province', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100, null=True)),
                ('rules', models.CharField(max_length=100, null=True)),
                ('date', models.DateTimeField()),
                ('time', models.TimeField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='tournament_images/')),
                ('location', models.CharField(max_length=255)),
                ('rounds', models.IntegerField(choices=[(1, '1 Round'), (2, '2 Rounds'), (3, '3 Rounds')], default=1, help_text='Number of rounds')),
                ('game_mode', models.CharField(choices=[('TimeAttack', 'Time Attack: Complete the objective in the shortest time possible.'), ('HighestScore', 'Highest Score: Achieve the highest score to win.')], default='TimeAttack', max_length=20)),
                ('tournament_type', models.CharField(choices=[('RoboSports', 'RoboSports: Teams design 2 robots that compete with robots of another team.'), ('RoboMission', 'RoboMission: Build and program a robot that solves challenges on a field.'), ('FutureEngineers', 'FutureEngineers: Highest Score: Achieve the highest score to win.'), ('FutureInnovators', 'FutureInnovators: Develop a robot project that helps solve real world problems.')], default='RoboSports', max_length=20)),
                ('video_url', models.URLField(blank=True, max_length=250, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_tournaments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('score_one', models.IntegerField(blank=True, null=True)),
                ('score_two', models.IntegerField(blank=True, null=True)),
                ('score_three', models.IntegerField(blank=True, null=True)),
                ('total_score', models.IntegerField(blank=True, null=True)),
                ('time_score_one', models.DurationField(blank=True, null=True)),
                ('time_score_two', models.DurationField(blank=True, null=True)),
                ('time_score_three', models.DurationField(blank=True, null=True)),
                ('time_total_score', models.DurationField(blank=True, null=True)),
                ('video_url', models.URLField(blank=True, max_length=250, null=True)),
                ('coach', models.CharField(blank=True, max_length=255, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_teams', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='teams', to='tournament_app.players')),
                ('tournament', models.ManyToManyField(related_name='teams', to='tournament_app.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Bracket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('state', models.JSONField(default=dict)),
                ('team', models.ManyToManyField(related_name='brackets', to='tournament_app.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brackets', to='tournament_app.tournament')),
            ],
        ),
    ]
