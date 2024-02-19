from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('first_api.urls')),
    path('api/v2/', include('models_with_api.urls')),
]
