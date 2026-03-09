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




# follow and unfollow views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):

    user_to_follow = User.objects.get(id=user_id)

    request.user.following.add(user_to_follow)

    return Response({"message": f"You are now following {user_to_follow.username}"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):

    user_to_unfollow = User.objects.get(id=user_id)

    request.user.following.remove(user_to_unfollow)

    return Response({"message": f"You unfollowed {user_to_unfollow.username}"})