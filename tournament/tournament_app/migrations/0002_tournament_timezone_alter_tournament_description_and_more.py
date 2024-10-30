# Generated by Django 5.0.6 on 2024-10-30 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='timezone',
            field=models.CharField(choices=[('America/Los_Angeles', 'PST'), ('America/New_York', 'EST'), ('America/Chicago', 'CST'), ('America/Denver', 'MST'), ('UTC', 'UTC')], default='UTC', max_length=500),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='game_mode',
            field=models.CharField(choices=[('TimeAttack', 'Time Attack: Complete the objective in the shortest time possible.'), ('HighestScore', 'Highest Score: Achieve the highest score to win.')], default='TimeAttack', max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='rules',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='tournament_type',
            field=models.CharField(choices=[('RoboSports', 'RoboSports: Teams design 2 robots that compete with robots of another team.'), ('RoboMission', 'RoboMission: Build and program a robot that solves challenges on a field.'), ('FutureEngineers', 'FutureEngineers: Highest Score: Achieve the highest score to win.'), ('FutureInnovators', 'FutureInnovators: Develop a robot project that helps solve real world problems.')], default='RoboSports', max_length=200),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='video_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
