from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home, name="home"),
    path("room/<str:pk>/", views.room , name = "room" ),
    
]
