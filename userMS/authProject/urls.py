
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('verifyToken/', views.UsuariosVerifyToken.as_view()),
    path('usuarios/', views.UsuariosCreateView.as_view()),
    path('usuarios/<int:pk>/', views.UsuariosDetailView.as_view()),
]   
