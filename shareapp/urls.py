from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('home/sucess/',views.sucess,name = 'sucess'),
    path('home/<str:key>/',views.download_file,name = 'download'),
]