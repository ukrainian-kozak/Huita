from django.shortcuts import render
from .models import Menu, Booking, MenuItem
from .serializer import MenuSerializer, BookingSerializer, UserSerializer, MenuItemSerializer
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]    


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 


# Create your views here.
def index(request):
    return render(request, 'index.html', {})