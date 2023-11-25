from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import BookViewSet

router = DefaultRouter()
router.register('book', BookViewSet, basename='book')

urlpatterns = router.urls
