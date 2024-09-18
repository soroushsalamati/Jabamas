from .models import Owner , Villa
from rest_framework.serializers import ModelSerializer


class VillaSerializer(ModelSerializer):
    class Meta:
        model = Villa
        fields = '__all__'


class OwnerSerializer(ModelSerializer):
    class Meta:
        model = Owner
        fields ='__all__'


