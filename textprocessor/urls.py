from django.urls import path
from textprocessor import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
]
