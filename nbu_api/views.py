from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Currency
from .serializers import CurrencySerializer
from rest_framework import status


class GetCurrencyAPIView(APIView):

    def get(self, request):
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(instance=currencies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
