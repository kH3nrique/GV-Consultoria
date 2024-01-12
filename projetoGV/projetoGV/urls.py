from django.urls import path
from appGV import views

urlpatterns = [
    #rota, view, nome de referência 
    path('', views.home, name='home'), 

    path('usuarios/', views.users, name='listagemUsuarios')
]