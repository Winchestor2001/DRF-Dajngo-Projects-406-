from django.urls import path
from .views import HelloApiView, FruitsAPIView


urlpatterns = [
    path('on/', HelloApiView.as_view()),
    path('fruits/', FruitsAPIView.as_view()),
]