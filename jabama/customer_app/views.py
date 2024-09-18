from rest_framework.generics import ListAPIView ,CreateAPIView ,ListCreateAPIView ,RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .models import Customer ,Reserve ,User ,Villa
from owner_app.serializers import VillaSerializer
from .serializers import ReserverSerializer ,UserSerializer ,ReserveSchduleSerializer, ReserveDateSerializer
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCustomer
from rest_framework.exceptions import ValidationError
from django.db import transaction


class Login(TokenObtainPairView):
    pass


class Refresh(TokenRefreshView):
    pass


class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        return Customer.objects.create(user=serializer.save() , wallet = 50.0)
    

class ReserveView(ListCreateAPIView):
    queryset = Reserve.objects.all()
    serializer_class = ReserverSerializer
    permission_classes = [IsAuthenticated ,IsCustomer]

    def get_queryset(self):
        my_customer = Customer.objects.get(user = self.request.user)
        return Reserve.objects.filter(customer = my_customer)
    

class ReserveDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Reserve.objects.all()
    serializer_class = ReserveDateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reserve.objects.filter(user=self.request.user)


class AllVilla(ListAPIView):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer


class VillaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Villa.objects.filter(user=self.request.user)


class VillaSchdule(ListAPIView):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSchduleSerializer
    def get_queryset(self):
        my_villa = self.request.data.get("villa ID")
        if not my_villa:
            raise ValidationError("villa ID is required")
        return Reserve.objects.filter(villa = my_villa)