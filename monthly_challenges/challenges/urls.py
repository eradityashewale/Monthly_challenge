from django.urls import path
from . import views

urlpatters = [
    path("January", views.index)
]