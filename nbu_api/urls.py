from django.urls import path
from .views import GetCurrencyAPIView


urlpatterns = [
    path('currency/', GetCurrencyAPIView.as_view())
]



