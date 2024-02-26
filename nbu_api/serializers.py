from rest_framework.serializers import ModelSerializer
from .models import Currency
from datetime import datetime


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        exclude = ['id']
    
    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata['date'] = datetime.strftime(instance.date, '%d-%m-%Y %H:%M:%S')
        return redata

