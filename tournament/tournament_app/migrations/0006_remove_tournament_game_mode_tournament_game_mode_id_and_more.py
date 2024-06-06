# Generated by Django 5.0.6 on 2024-06-06 20:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('tournament_app', '0005_alter_gamemode_time_limit'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='game_mode',
        ),
        migrations.AddField(
            model_name='tournament',
            name='game_mode_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='game_mode_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.CreateModel(
            name='HybridGameMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('event_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rounds', models.IntegerField(choices=[(1, '1 Round'), (2, '2 Rounds'), (3, '3 Rounds')], default=1, help_text='Number of rounds')),
                ('time_score', models.DurationField(blank=True, help_text='Time limit (minutes and seconds)', null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hybrid_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScoreBasedGameMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('event_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rounds', models.IntegerField(choices=[(1, '1 Round'), (2, '2 Rounds'), (3, '3 Rounds')], default=1, help_text='Number of rounds')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_based_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimeBasedGameMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('event_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rounds', models.IntegerField(choices=[(1, '1 Round'), (2, '2 Rounds'), (3, '3 Rounds')], default=1, help_text='Number of rounds')),
                ('time_score', models.DurationField(blank=True, help_text='Time limit (minutes and seconds)', null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_based_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Bracket',
        ),
        migrations.DeleteModel(
            name='GameMode',
        ),
    ]