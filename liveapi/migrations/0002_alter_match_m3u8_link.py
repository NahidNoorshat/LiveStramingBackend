# Generated by Django 5.0 on 2024-06-16 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("liveapi", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="match",
            name="m3u8_link",
            field=models.TextField(),
        ),
    ]
