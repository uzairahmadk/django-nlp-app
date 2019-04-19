from django.urls import path
from django.views.decorators.cache import never_cache
from textprocessor import views

urlpatterns = [
    path('tag/', never_cache(views.TagProcessorView.as_view()), name='tag-processor-page'),
    path('noun/', never_cache(views.NounProcessorView.as_view()), name='noun-processor-page'),
    path('word/', never_cache(views.WordProcessorView.as_view()), name='word-processor-page'),
    path('sentence/', never_cache(views.SentenceProcessorView.as_view()), name='sentence-processor-page'),
]
