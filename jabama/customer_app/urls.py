from django.urls import path
from .views import Login , Register, ReserveView , VillaSchdule , AllVilla


urlpatterns = [
    path("login/" , Login.as_view()),
    path("reserve/" , ReserveView.as_view()),
    path("register/" , Register.as_view()),
    path("all-villa/" , AllVilla.as_view()),
    path("schdule/" , VillaSchdule.as_view()),
]