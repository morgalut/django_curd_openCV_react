import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.urls import reverse  # Import reverse to construct URLs

@pytest.mark.django_db
def test_image_conversion(mocker):
    user = User.objects.create_user(username='testuser', password='password123')
    client = APIClient()
    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    # Mock the OpenCV function
    mocker.patch('items.opencv_utils.image_processing.convert_to_grayscale', return_value=None)

    data = {
        'input_image_path': r"C:\Users\Mor\Desktop\picture\WhatsApp Image 2024-08-15 at 09.09.27_2ecf96b2.jpg",
        'output_image_path': r"C:\Users\Mor\Desktop\picture\WhatsApp Image 2024-08-15 at 09.09.27_2ecf96b2.jpg"
    }

    response = client.post(reverse('convert-image'), data, format='json')  # Use reverse to get the URL
    
    assert response.status_code == 200
    # You can check the response content if necessary
    assert response['Content-Disposition'] is not None  # Check if the file is returned
