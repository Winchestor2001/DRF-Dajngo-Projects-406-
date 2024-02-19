from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Persone


class AllPersonsAPIView(APIView):

    def get(self, request):
        workers = Persone.objects.all()
        return Response({"workers": workers})
