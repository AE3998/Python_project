from django.urls import path
from . import views

urlpatterns = [
    # Dirigia al archivo views, acceder a la funcion index 
    # como el archivo de html
    path('', views.index, name = 'index')
]