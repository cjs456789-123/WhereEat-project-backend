from django.urls import path
from . import views

urlpatterns = [
    # path('', views.dataFromKakaoapi, name='dataFromKakaoapi'),
    
    # 230220-FE 합치기
    path('', views.main, name='main'),
    path('listup/', views.listup, name='listup'),
    path('map/', views.map, name='map'),
]