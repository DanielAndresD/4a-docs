from django.db.models.base import ModelStateFieldsCacheDescriptor
from rest_framework.response import Response
from rest_framework import views
from authApp.models.usuarios import usuarios
from authApp.serializers.usuarios_serializer import Mostrarusuarios_serializer, Crearusuarios_serializer


class usuariosview(views.APIView):
    def get (self, requerest):
        lista_usuarios = usuarios.objects.all()
        serializers = Mostrarusuarios_serializer(lista_usuarios, many=True)
        return Response(serializers.data, 200)

 
    def post(self, request):
        datos_json = request.data
        serializers = Crearusuarios_serializer(data=datos_json)
        if serializers.is_valid():
            serializers.save()
            return Response({"mensaje": "Usuario creado"}, 200)       
        else:
            return Response(serializers.errors, 405)

    
    def delete(self, request, pk):
        try:
            Psp_App = usuarios.objects.get(pk=pk)
            Psp_App.delete()
            return Response({"mensaje": "Usuario borrado"}, 200)
        except:
            return Response({"mensaje": "Usuario no existe"}, 400)