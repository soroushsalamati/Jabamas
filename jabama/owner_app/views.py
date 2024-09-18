from rest_framework.generics import ListAPIView , CreateAPIView
from .serializers import *
from . models import Villa , Owner
from rest_framework.permissions import IsAuthenticated


class NewVilla(CreateAPIView):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer
    permission_classes = [IsAuthenticated]


class AllVilla(ListAPIView):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer


class MyVilla(ListAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Owner.objects.filter(user = self.request.user)