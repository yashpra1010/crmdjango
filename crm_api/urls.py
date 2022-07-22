#from django.conf.urls import url
from django.urls import path, include
from crm_api import views

urlpatterns = [
    path('cust-api', views.cust_api_view.as_view()),
    path('product-api', views.prod_api_view.as_view()),
    path('order-api', views.order_api_view.as_view()),
    path('cust-api/<str:pk>/', views.cust_detail_api_view.as_view()),
    path('product-api/<str:pk>/', views.prod_detail_api_view.as_view()),
    path('order-api/<str:pk>/', views.order_detail_api_view.as_view()),
]