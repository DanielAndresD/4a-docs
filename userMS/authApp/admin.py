from django.contrib import admin

# Register your models here.
from .models.usuarios import usuarios
admin.site.register(usuarios)