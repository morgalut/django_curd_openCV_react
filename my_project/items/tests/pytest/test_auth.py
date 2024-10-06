import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

@pytest.mark.django_db
def test_register_user():
    client = APIClient()
    data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    }
    response = client.post('/register/', data, format='json')
    assert response.status_code == 201
    assert 'token' in response.data

@pytest.mark.django_db
def test_login_user():
    client = APIClient()
    User.objects.create_user(username='testuser', password='password123')

    data = {'username': 'testuser', 'password': 'password123'}
    response = client.post('/login/', data, format='json')

    assert response.status_code == 200
    assert 'token' in response.data
