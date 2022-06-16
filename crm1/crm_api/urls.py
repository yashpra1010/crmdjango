#from django.conf.urls import url
from django.urls import path, include
from crm_api import views

urlpatterns = [
    path('api', views.crm_api_view.as_view()),
    path('api/<str:pk>/', views.crm_detail_api_view.as_view()),
]