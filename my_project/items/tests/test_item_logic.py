from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from items.models import Item
from django.urls import reverse

class ItemLogicTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)
        self.item = Item.objects.create(name="Test Item", description="Test description", created_by=self.user)

    def test_create_item(self):
        url = reverse('item-list')
        data = {'name': 'New Item', 'description': 'New Description'}
        response = self.client.post(url, data, format='json')
        
        # Assert item creation
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)

    def test_get_items(self):
        url = reverse('item-list')
        response = self.client.get(url, format='json')
        
        # Assert the response contains the created item
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Test Item")

    def test_update_item(self):
        url = reverse('item-detail', kwargs={'pk': self.item.id})
        data = {'name': 'Updated Item', 'description': 'Updated Description'}
        response = self.client.put(url, data, format='json')

        # Assert that the item is updated successfully
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, 'Updated Item')

    def test_delete_item(self):
        url = reverse('item-detail', kwargs={'pk': self.item.id})
        response = self.client.delete(url)

        # Assert that the item is deleted successfully
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0)

    def test_retrieve_nonexistent_item(self):
        url = reverse('item-detail', kwargs={'pk': 999})  # A non-existent ID
        response = self.client.get(url)

        # Assert that a 404 response is returned
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
