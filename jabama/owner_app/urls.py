from django.urls import path
from .views import NewVilla , AllVilla , MyVilla


urlpatterns = [
    path("my-villa/" , MyVilla.as_view()),
    path("all-villa/" , AllVilla.as_view()),
    path("new-villa/" , NewVilla.as_view()),
]