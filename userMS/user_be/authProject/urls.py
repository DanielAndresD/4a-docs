from django.contrib import admin
from django.urls import path
from authApp.views.usuariosview import usuariosview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', usuariosview.as_view()),
    path('usuarios/<int:pk>', usuariosview.as_view()),
]
