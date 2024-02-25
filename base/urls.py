from django.urls import path
from . import views

urlpatterns = [
 path("home/", views.home),
 path("room/", views.room),
 path("school/", views.school)
]