from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home, name="home"),
    path("room/<str:pk>/", views.room , name = "room" ),
    path("create-room", views.createRoom , name = "create-room" ),
    path("update-room/<str:pk>", views.updateRoom , name = "update-room" ),
    path("delete-record/<str:pk>", view=views.deleteRoom, name='delete-room')
    
]
