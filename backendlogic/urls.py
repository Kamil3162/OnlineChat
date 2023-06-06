from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('register', views.Register.as_view(), name="register"),
    path('login', views.Login.as_view(), name="login"),
    path('logout', views.Logout.as_view(), name="logout"),
    path('room_create', views.RoomCreate.as_view(), name="room_create"),
    path('room/<int:id>', views.Room.as_view(), name="room_detail")
]