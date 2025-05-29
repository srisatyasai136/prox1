from django.urls import path
from . import views

urlpatterns = [
    path("receive_message/", views.receive_message),
    path("get_latest_message/", views.get_latest_message),
]