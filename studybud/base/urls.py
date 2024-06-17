from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home, name="home"),
    path("room/<str:pk>/", views.room , name = "room" ),
    path("profile/<str:pk>/", views.userProfile, name = "user-profile"),



    path("create-room", views.createRoom , name = "create-room" ),
    path("update-room/<str:pk>", views.updateRoom , name = "update-room" ),
    path("delete-record/<str:pk>", view=views.deleteRoom, name='delete-room'),
    path("login", view=views.loginPage, name='login'),
    path("logout", view=views.logoutUser, name='logout'),
     path("register", view=views.registerPage, name='register'),
     path("delete-message/<str:pk>", view=views.deleteMessage, name='delete-message'),
    path('update-user/<str:pk>/', views.update_user, name='update-user'),
    
    
]
