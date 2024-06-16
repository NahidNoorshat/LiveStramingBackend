# Generated by Django 5.0 on 2024-06-16 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Match",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sport_type",
                    models.CharField(
                        choices=[
                            ("Football", "Football"),
                            ("Basketball", "Basketball"),
                            ("Others", "Others"),
                        ],
                        max_length=50,
                    ),
                ),
                ("team1_name", models.CharField(max_length=100)),
                ("team2_name", models.CharField(max_length=100)),
                ("team1_image", models.ImageField(upload_to="team_images/")),
                ("team2_image", models.ImageField(upload_to="team_images/")),
                ("m3u8_link", models.URLField()),
            ],
        ),
    ]