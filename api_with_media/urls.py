from django.urls import path
from .views import CreateJoraAPIView


urlpatterns = [
    path('add_jora/', CreateJoraAPIView.as_view()),
]