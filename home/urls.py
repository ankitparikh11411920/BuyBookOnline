from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('category/', views.category),
    path('allproducts/', views.allProducts),
    path('logout/', views.logout),
    path('order/', views.order),
    path('yourorders/', views.yourorders)
]