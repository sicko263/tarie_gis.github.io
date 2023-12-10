from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path
from agric import views

urlpatterns = [
    path('', views.index, name='index'),
    path('farm-master-search/<str:search_option>/', views.MapSearch, name='farm-master-search'),
]