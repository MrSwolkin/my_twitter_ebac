# Generated by Django 5.0.4 on 2024-05-15 13:55

import django.contrib.auth.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("twitter", "0002_alter_profile_bio"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="date_modified",
            field=models.DateField(
                default=django.utils.timezone.now,
                verbose_name=django.contrib.auth.models.User,
            ),
        ),
    ]
