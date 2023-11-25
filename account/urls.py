from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import CreateUser

urlpatterns = [
    path("", CreateUser.as_view()),

]
