from django.urls import path
from .views import MatchListCreate, MatchDetail

urlpatterns = [
    path('matches/', MatchListCreate.as_view(), name='match-list-create'),
    path('matches/<int:pk>/', MatchDetail.as_view(), name='match-detail'),
]
