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

def get(self, request, *args, **kwargs): 
     
        token = request.META.get('HTTP_AUTHORIZATION')[7:] 
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM']) 
        valid_data = tokenBackend.decode(token,verify=False) 
 
        if valid_data['user_id'] != kwargs['pk']: 
            stringResponse = {'detail':'Unauthorized Request'} 
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) 
        return super().get(request, *args, **kwargs)