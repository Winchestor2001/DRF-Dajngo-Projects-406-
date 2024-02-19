from rest_framework.serializers import ModelSerializer
from .models import Persone, Profession


class AllProfessionsSerializer(ModelSerializer):
    
    class Meta:
        model = Profession
        fields = '__all__'


class AllPersonsSerializer(ModelSerializer):
    profession = AllProfessionsSerializer()

    class Meta:
        model = Persone
        fields = '__all__'
        # fields = ['full_name', 'age', 'address']
        # exclude = ['age']


