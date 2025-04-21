from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DepositRequestSerializer

class DepositRequestView(APIView):
    def post(self, request):
        # Serialize the deposit request
        serializer = DepositRequestSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            # Save deposit request
            deposit = serializer.save()
            
            # Simulate deposit confirmation (immediate instead of background task)
            deposit.status = "confirmed"
            deposit.save()

            return Response({"id": deposit.id, "status": deposit.status}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
