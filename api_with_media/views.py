from rest_framework.views import APIView
from .models import Jora
from rest_framework.response import Response
from .serializers import JoraSerializer
from rest_framework import status


class CreateJoraAPIView(APIView):
    
    def post(self, request):
        serializer = JoraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







