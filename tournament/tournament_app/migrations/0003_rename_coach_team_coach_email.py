# Generated by Django 5.0.6 on 2024-07-04 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament_app', '0002_alter_tournament_rounds'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='coach',
            new_name='coach_email',
        ),
    ]
