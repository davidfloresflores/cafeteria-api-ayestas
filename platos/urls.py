
from django.urls import path
from .views import estado, lista_platos, detalle_plato

urlpatterns = [
    path('estado/', estado, name='estado'),
    path('platos/', lista_platos, name='lista_platos'),
    path('platos/<int:id>/', detalle_plato, name='detalle_plato'),
]
