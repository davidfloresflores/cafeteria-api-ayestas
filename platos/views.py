
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .datos import platos


# R2 - Estado de la API
@api_view(['GET'])
def estado(request):
    return Response({
        "app": "Cafetería UTLA",
        "version": "1.0"
    })


# R3 y R5 - Listar y registrar platos
@api_view(['GET', 'POST'])
def lista_platos(request):

    if request.method == 'GET':
        return Response(platos)

    if request.method == 'POST':

        nombre = request.data.get('nombre')
        precio = request.data.get('precio')

        if nombre is None or precio is None:
            return Response(
                {"error": "Nombre y precio son obligatorios"},
                status=status.HTTP_400_BAD_REQUEST
            )

        nuevo_id = max(
            [plato["id"] for plato in platos],
            default=0
        ) + 1

        nuevo_plato = {
            "id": nuevo_id,
            "nombre": nombre,
            "precio": precio
        }

        platos.append(nuevo_plato)

        return Response(
            nuevo_plato,
            status=status.HTTP_201_CREATED
        )


# R4 - Consultar plato por ID
@api_view(['GET'])
def detalle_plato(request, id):

    for plato in platos:
        if plato["id"] == id:
            return Response(
                plato,
                status=status.HTTP_200_OK
            )

    return Response(
        {"error": "Plato no encontrado"},
        status=status.HTTP_404_NOT_FOUND
    )
