from django.db import models

class SportType(models.TextChoices):
    FOOTBALL = 'Football'
    BASKETBALL = 'Basketball'
    OTHERS = 'Others'

class Match(models.Model):
    sport_type = models.CharField(max_length=50, choices=SportType.choices)
    team1_name = models.CharField(max_length=100)
    team2_name = models.CharField(max_length=100)
    team1_image = models.ImageField(upload_to='team_images/')
    team2_image = models.ImageField(upload_to='team_images/')
    m3u8_link = models.TextField() 

    def __str__(self):
        return f"{self.team1_name} vs {self.team2_name}"

