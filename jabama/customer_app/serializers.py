from .models import Reserve ,Customer ,User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class ReserverSerializer(ModelSerializer):
    class Meta:
        model = Reserve
        fields = '__all__'


class ReserveSchduleSerializer(ModelSerializer):
    class Meta:
        model = Reserve
        fields = ["start_time","finish_time"]


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']


class ReserveDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = "__all__"
        