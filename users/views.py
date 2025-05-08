from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Modify this view to provide a custom message when the user is not logged in
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "email": request.user.email,
            "is_staff": request.user.is_staff,
            "is_superuser": request.user.is_superuser,
            "id": request.user.id,
        })

# Custom Login View to provide "Please log in" message
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if logged in
    return render(request, 'login.html', {'message': 'Please log in to access this page.'})
