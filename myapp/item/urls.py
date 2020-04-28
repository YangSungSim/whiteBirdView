from django.urls import path, include
from .views import *
urlpatterns = [
    path('index/',index,name='indexs'),
    path('index/new/',post,name='post')
]