# django_sitestatus/urls.py
from django.urls import path
from .views import change_site_status

urlpatterns = [
    path('change-site-status', change_site_status, name='change_site_status'),
]