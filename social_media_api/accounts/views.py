from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    # This view handles user registration
    serializer_class = UserSerializer

class LoginView(ObtainAuthToken):
    # This view handles user login and returns a token
    pass

# Ensure you also have a ProfileView if your URLs require it
