from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='whatsonzambia-home'),
    path('about/', views.about, name='whatsonzambia-about'),
]