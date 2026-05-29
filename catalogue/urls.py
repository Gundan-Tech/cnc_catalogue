from django.urls import path
from . import views

urlpatterns = [
    # The empty string '' means this is the homepage of your catalogue
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]