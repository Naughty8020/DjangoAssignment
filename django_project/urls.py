# django_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('psys.urls')),  # ← psys アプリのルーティングを読み込む
]
