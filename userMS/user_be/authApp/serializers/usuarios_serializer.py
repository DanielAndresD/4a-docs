from rest_framework import serializers
from authApp.models.usuarios import usuarios


class usuarios_serializer(serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields = ["id", "Nombres", "Apellidos", "No_documento", "Direccion", "Telefono", "Correo", "Ciudad"]
