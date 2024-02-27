from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu
from .serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Add a few test instances of the Menu model
        Menu.objects.create(name='Item 1', description='Description 1', price=10.99)
        Menu.objects.create(name='Item 2', description='Description 2', price=15.99)

    def test_getall(self):
        client = APIClient()
        url = reverse('menu-list')  # Assuming you have defined the URL pattern for menu list view

        # Retrieve all Menu objects added for the test purpose
        response = client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)