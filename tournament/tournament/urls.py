# tournament/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tournament_app.urls')),  # Include tournaments app URLs
    path('accounts/', include('allauth.urls')),  # Include allauth URLs
]
