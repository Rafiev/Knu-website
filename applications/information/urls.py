from django.urls import path

from .views import CompoundAPIView, CompoundDetailAPIView ,NewsAPIView, NewsDetailAPIView


urlpatterns = [
    path('compounds/', CompoundAPIView.as_view(), name='compound-post'),
    path('compounds/<int:com_id>/', CompoundDetailAPIView.as_view(), name='compound-detail'),
    path('news/', NewsAPIView.as_view(), name='news-post'),
    path('news/<int:new_id>/', NewsDetailAPIView.as_view(), name='news-detail'),
]