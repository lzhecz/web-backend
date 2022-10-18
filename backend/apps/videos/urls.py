from django.urls import path
from .views import VideosAPIView

app_name = 'videos'

urlpatterns = [
    path('latest/', VideosAPIView.as_view())
]