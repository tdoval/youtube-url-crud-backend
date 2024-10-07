import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from urls.infrastructure.repositories import VideoURLRepository

def create_user_and_get_token(username='testuser', password='testpass123'):
    user = User.objects.create_user(username=username, password=password)
    client = APIClient()
    response = client.post('/api/token/', {'username': username, 'password': password})
    return client, response.data['access']

@pytest.mark.django_db
def test_user_registration():
    client = APIClient()
    response = client.post('/api/register/', {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password': 'testpass123'
    })
    assert response.status_code == 201
    assert User.objects.filter(username='newuser').exists()

@pytest.mark.django_db
def test_jwt_authentication():
    client, access_token = create_user_and_get_token()
    assert access_token is not None

@pytest.mark.django_db
def test_crud_videourl():
    client, access_token = create_user_and_get_token()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    response = client.post('/api/videos/', {'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'})
    assert response.status_code == 201

    video = VideoURLRepository.get_all_videos().first()
    assert video is not None

    video_id = str(video.id)
    response = client.delete(f'/api/videos/{video_id}/')
    assert response.status_code == 204

    deleted_video = VideoURLRepository.get_video_by_id(video_id)
    assert deleted_video is None

@pytest.mark.django_db
def test_update_videourl():
    client, access_token = create_user_and_get_token()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    response = client.post('/api/videos/', {'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'})
    assert response.status_code == 201

    video = VideoURLRepository.get_all_videos().first()
    video_id = str(video.id)

    response = client.patch(f'/api/videos/{video_id}/update/', {
        'url': 'https://www.youtube.com/watch?v=9bZkp7q19f0'
    }, format='json')
    assert response.status_code == 200

    updated_video = VideoURLRepository.get_video_by_id(video_id)
    assert updated_video.url == 'https://www.youtube.com/watch?v=9bZkp7q19f0'
