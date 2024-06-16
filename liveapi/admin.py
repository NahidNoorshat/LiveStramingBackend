from django.contrib import admin
from .models import Match

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('sport_type', 'team1_name', 'team2_name', 'm3u8_link')
    search_fields = ('team1_name', 'team2_name', 'sport_type')

