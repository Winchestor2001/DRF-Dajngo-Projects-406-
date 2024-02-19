from django.urls import path
from .views import AllPersonsAPIView


urlpatterns = [
    path('workers/', AllPersonsAPIView.as_view()),
]