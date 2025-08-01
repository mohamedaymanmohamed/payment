# payments/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save-order/', views.save_order, name='save_order'),
]
