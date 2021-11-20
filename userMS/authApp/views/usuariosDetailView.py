from rest_framework import generics
from authApp.models.usuarios import usuarios
from authApp.serializers.usuarios_serializer import usuarios_serializer

class UsuariosDetailView(generics.RetrieveAPIView):
    queryset = usuarios.objects.all()
    serializer_class = usuarios_serializer
    
    def get (self, requerest):
        lista_usuarios = usuarios.objects.all()
        serializers = usuarios_serializer(lista_usuarios, many=True)
        return Response(serializers.data, 200)
