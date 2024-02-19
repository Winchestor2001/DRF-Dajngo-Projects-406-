from django.urls import path
from .views import AllPersonsAPIView, AllProfessionsAPIView


urlpatterns = [
    path('workers/', AllPersonsAPIView.as_view()),
    path('professions/', AllProfessionsAPIView.as_view()),
]