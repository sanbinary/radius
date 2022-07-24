# Generated by Django 4.0.3 on 2022-04-26 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subscription',
            name='stripe_subscription',
            field=models.CharField(blank=True, max_length=105, null=True),
        ),
    ]
