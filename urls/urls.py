from django.urls import path
from urls.interfaces.views import VideoURLListCreateView, VideoURLDeleteView
from urls.interfaces.views import UserRegistrationView

urlpatterns = [
    path('videos/', VideoURLListCreateView.as_view(), name='video-list-create'),

    path('videos/<int:pk>/', VideoURLDeleteView.as_view(), name='video-delete'),

    path('register/', UserRegistrationView.as_view(), name='user-registration'),
]