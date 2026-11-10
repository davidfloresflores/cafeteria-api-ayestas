
from django.urls import path
from .views import estado, lista_platos

urlpatterns = [
    path('estado/', estado, name='estado'),
    path('platos/', lista_platos, name='lista_platos'),
]
