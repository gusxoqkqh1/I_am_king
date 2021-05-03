from django.urls import path 
from .views import ProductDetailView, MainView

urlpatterns =[
        path('/product',MainView.as_view()),
        path('/product/<int:product_id>', ProductDetailView.as_view())
    
     ]

