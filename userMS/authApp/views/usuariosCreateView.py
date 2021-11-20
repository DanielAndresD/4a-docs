from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.serializers.usuarios_serializer import usuarios_serializer

class UsuariosCreateView(views.APIView):

    def post(self, request):
        datos_json = request.data
        serializers = usuarios_serializer(data=datos_json)
        if serializers.is_valid():
            serializers.save()
            return Response({"mensaje": "Usuario creado"}, 200)       
        else:
            return Response(serializers.errors, 405)
        
        tokenData = {"username":request.data["username"],
        "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
