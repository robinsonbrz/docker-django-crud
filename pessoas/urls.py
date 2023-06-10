from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pessoas, name='pessoas'),
    path('salvar/', views.salvar, name='salvarpessoa'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
