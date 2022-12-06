from django.urls import path
from . import views

# have same variable names, so that it matches
urlpatterns = [

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path("", views.home, name="home"),
    path("room/<str:pk>/", views.room, name="room"),
    path('profile/<str:pk>', views.userProfile, name="user-profile"),

    path('create-room/', views.create_room, name="create-room"),
    path('update-room/<str:pk>', views.updated_room, name="update-room"),
    path('delete-room/<str:pk>', views.delete_room, name="delete-room"),
    path('delete-message/<str:pk>', views.delete_message, name="delete-message"),
    path('update-user/', views.updateUser, name="update-user"),
    path('topics/', views.topics_page, name="topics"),
    path('activity/', views.activity_page, name="activity"),

]
