from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Persone, Profession
from .serializers import AllPersonsSerializer, AllProfessionsSerializer


class AllPersonsAPIView(APIView):

    def get(self, request):
        workers = Persone.objects.all()
        serializer = AllPersonsSerializer(instance=workers, many=True)
        return Response({"workers": serializer.data})
    

class AllProfessionsAPIView(APIView):

    def get(self, request):
        workers = Profession.objects.all()
        serializer = AllProfessionsSerializer(instance=workers, many=True)
        return Response({"professions": serializer.data})


