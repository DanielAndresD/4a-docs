from django.db.models.base import ModelStateFieldsCacheDescriptor
from rest_framework.response import Response
from django.conf import settings
from rest_framework import views
from rest_framework import generics, status 
from authApp.models.usuarios import usuarios
from rest_framework_simplejwt.backends import TokenBackend 
from authApp.serializers.usuarios_serializer import Mostrarusuarios_serializer, Crearusuarios_serializer
from rest_framework.permissions import IsAuthenticated 

from authApp.models.usuarios import usuarios
from authApp.serializers.usuarios_serializer import UserSerializer 

class usuariosview(views.APIView):
    queryset = usuarios.objects.all() 
    serializer_class = UserSerializer 
    permission_classes = (IsAuthenticated,) 


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

    
    def get(self, request, *args, **kwargs): 
     
        token = request.META.get('HTTP_AUTHORIZATION')[7:] 
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM']) 
        valid_data = tokenBackend.decode(token,verify=False) 
 
        if valid_data['user_id'] != kwargs['pk']: 
            stringResponse = {'detail':'Unauthorized Request'} 
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) 
         
        return super().get(request, *args, **kwargs) 