from django.urls import path
from . import views

urlpatterns = [
    path('', views.teams_list, name='teams'),
    path('teams/<int:pk>/', views.team_details, name='team_details')
]