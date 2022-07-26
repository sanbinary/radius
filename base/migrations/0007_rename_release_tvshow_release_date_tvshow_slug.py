# Generated by Django 4.0.3 on 2022-06-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_movie_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tvshow',
            old_name='release',
            new_name='release_date',
        ),
        migrations.AddField(
            model_name='tvshow',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
