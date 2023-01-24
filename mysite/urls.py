# mysite/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("chat/", include("chat.urls")),
    path("", include("shareapp.urls")),
    path("admin/", admin.site.urls),
]