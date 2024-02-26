from rest_framework.views import APIView
from .models import Jora
from rest_framework.response import Response
from .serializers import JoraSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class CreateJoraAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        jora_list = Jora.objects.all()

        if 'q' in request.GET:
            jora_list = jora_list.filter(description__icontains=request.GET['q'])

        serializer = JoraSerializer(instance=jora_list, many=True)

        return Response({"Jora": serializer.data}, status=status.HTTP_202_ACCEPTED)
    
    def post(self, request):
        serializer = JoraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







