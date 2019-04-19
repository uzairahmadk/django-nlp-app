from django.urls import path
from textprocessor import views

urlpatterns = [
    path('', views.TagProcessorView.as_view(), name='tag-processor-page'),
]
