from rest_framework import serializers
from authApp.models.usuarios import usuarios


class Crearusuarios_serializer(serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields = ["id", "Nombres", "Apellidos", "No_documento", "Direccion", "Telefono", "Correo", "Ciudad"]

     
class Mostrarusuarios_serializer(serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields = ["id", "Nombres", "Apellidos", "No_documento", "Direccion", "Telefono", "Correo", "Ciudad"]
