from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('register', views.RegisterView.as_view(), name="register"),
    path('login', views.Login.as_view(), name="login"),
    path('logout', views.Logout.as_view(), name="logout"),
    path('room_create', views.RoomCreateView.as_view(), name="room_create"),
    path('room/<int:pk>/', views.RoomView.as_view(), name="room_detail"),
    path('rooms', views.RoomsView.as_view(), name="room_list"),
]