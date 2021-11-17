from rest_framework import generics, status

from authApp.models.usuarios import Usuarios
from authApp.serializers.userSerializer import UserSerializer

class UsuariosDetailView(generics.RetrieveAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UserSerializer
    