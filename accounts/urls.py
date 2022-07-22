from django.urls import path
from . import views
urlpatterns = [
    #Dashboard URL Router
    path('',views.home, name="home"),
    path('user/',views.userPage, name="user-page"),

    #Login & Register URL Router
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutPage, name="logout"),
    path('register/',views.registerPage, name="register"),

    #Products & Customer URL Router
    path('products/',views.products, name="products"),
    path('customer/<str:pk>/',views.customer, name="customer"),
    
    #CRUD URL Router
    path('create_order/<str:pk>/',views.createOrder, name="create_order"),
    path('update_order/<str:pk>/',views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/',views.deleteOrder, name="delete_order"),

    path('account/', views.accountSettings, name="account"),
]
