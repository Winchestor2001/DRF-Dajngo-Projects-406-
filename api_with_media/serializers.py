from rest_framework.serializers import ModelSerializer
from .models import Jora


class JoraSerializer(ModelSerializer):

    class Meta:
        model = Jora
        fields = '__all__'




