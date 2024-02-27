from .models import Menu, MenuItem
from rest_framework import serializers
from django.contrib.auth.models import User


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'no_of_guests', 'booking_date']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = "__all__"
        fields = ['id', 'title', 'price', 'inventory']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
