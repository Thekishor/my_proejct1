
from django.urls import path , include
from .import views

urlpatterns = [
  # path('index/', views.index_page , name='index_page'),
  path('', views.home_page , name='home_page'),
]