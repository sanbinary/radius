# Generated by Django 4.0.3 on 2022-05-01 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='type',
            field=models.CharField(choices=[('Null', 'N'), ('Movies', 'M'), ('TVShows', 'T')], default='N', max_length=15),
        ),
    ]
