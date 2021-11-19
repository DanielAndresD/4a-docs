from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.serializers.usuarios_serializer import usuarios_serializer

class UsuariosCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = usuarios_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"username":request.data["username"],
        "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)