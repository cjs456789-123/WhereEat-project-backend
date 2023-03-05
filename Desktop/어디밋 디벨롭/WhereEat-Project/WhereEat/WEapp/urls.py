from django.urls import path
from . import views

urlpatterns = [
    # 230220-FE합치기
    path('', views.main, name='main'),
    path('map', views.map, name='map'),
    path('listup', views.listup, name='listup'),
]