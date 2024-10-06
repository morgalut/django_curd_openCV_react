# Correct import of Token
from rest_framework.authtoken.models import Token
import pytest
from django.contrib.auth.models import User
from items.models.item_model import Item
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_create_item():
    user = User.objects.create_user(username='testuser', password='password123')
    client = APIClient()
    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    data = {'name': 'Test Item', 'description': 'Test Description'}
    response = client.post('/items/', data, format='json')

    assert response.status_code == 201
    assert Item.objects.count() == 1

@pytest.mark.django_db
def test_list_items():
    user = User.objects.create_user(username='testuser', password='password123')
    Item.objects.create(name='Item1', description='Desc1', created_by=user)
    client = APIClient()
    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    response = client.get('/items/')
    assert response.status_code == 200
    assert len(response.data) == 1
