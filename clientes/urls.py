from django.urls import path
from . import views

urlpatterns = [ 
    path('template/', views.template, name='template'),
    #path('', views.main, name='main'),
    path('', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro/listagem/', views.novocad, name='listagem'),
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/detalhes/<int:id>', views.detalhes, name='detalhes'),
]