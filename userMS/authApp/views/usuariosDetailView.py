from rest_framework import generics, status

from authApp.models.usuarios import Usuarios
from authApp.serializers.usuarios_serializer import usuarios_serializer

class UsuariosDetailView(generics.RetrieveAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = usuarios_serializer