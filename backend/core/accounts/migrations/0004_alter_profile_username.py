# Generated by Django 4.2.17 on 2025-01-06 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_recoverycode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="username",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
