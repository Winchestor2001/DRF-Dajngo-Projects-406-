from rest_framework.serializers import ModelSerializer
from .models import Jora


class JoraSerializer(ModelSerializer):

    class Meta:
        model = Jora
        fields = '__all__'


    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata['image'] = "http://127.0.0.1:8000" + instance.image.url
        return redata
    
