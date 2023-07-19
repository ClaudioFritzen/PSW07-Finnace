from django.urls import path
from . import views

urlpatterns = [
    path('novo_valor/', views.novo_valor, name="novo_valor"),
    path('views_extrato/', views.views_extrato, name='views_extrato'),
    
]