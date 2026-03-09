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
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

CustomUser = get_user_model()


class FollowUserView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]

    queryset = CustomUser.objects.all()

    def post(self, request, user_id):

        user_to_follow = CustomUser.objects.get(id=user_id)

        request.user.following.add(user_to_follow)

        return Response(
            {"message": f"You are now following {user_to_follow.username}"},
            status=status.HTTP_200_OK
        )


class UnfollowUserView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]

    queryset = CustomUser.objects.all()

    def post(self, request, user_id):

        user_to_unfollow = CustomUser.objects.get(id=user_id)

        request.user.following.remove(user_to_unfollow)

        return Response(
            {"message": f"You unfollowed {user_to_unfollow.username}"},
            status=status.HTTP_200_OK
        )