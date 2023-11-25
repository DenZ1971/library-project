
from .models import User
from .serializers import UserSerializer
from .tasks import send_welcome_email
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateUser(generics.CreateAPIView):
        serializer_class = UserSerializer
        queryset = User.objects.all()

        def perform_create(self, serializer):
                user = serializer.save()
                send_welcome_email.delay(user.email)


