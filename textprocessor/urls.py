from django.urls import path
from textprocessor import views

urlpatterns = [
    path('tag/', views.TagProcessorView.as_view(), name='tag-processor-page'),
    path('noun/', views.NounProcessorView.as_view(), name='noun-processor-page'),
]
