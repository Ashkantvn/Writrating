# Generated by Django 4.2.20 on 2025-04-03 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "__first__"),
        ("blogs", "0011_alter_blogresponse_response_to"),
    ]

    operations = [
        migrations.DeleteModel(
            name="BlogResponse",
        ),
        migrations.CreateModel(
            name="BlogResponse",
            fields=[],
            options={
                "verbose_name": "Blog Response",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("core.response",),
        ),
    ]
