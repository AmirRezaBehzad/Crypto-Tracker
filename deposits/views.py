from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DepositRequestSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Deposit, DepositRequest
from .serializers import DepositSerializer

class DepositRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = DepositRequest.objects.filter(user=request.user)
        serializer = DepositRequestSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepositRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DepositView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = Deposit.objects.filter(user=request.user)
        serializer = DepositSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepositSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

