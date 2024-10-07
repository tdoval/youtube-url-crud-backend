from django.urls import path
from urls.interfaces.views import VideoURLListCreateView, VideoURLDeleteView, VideoURLUpdateView, UserRegistrationView

urlpatterns = [
    path('videos/', VideoURLListCreateView.as_view(), name='video-list-create'),
    path('videos/<uuid:pk>/', VideoURLDeleteView.as_view(), name='video-delete'),
    path('videos/<uuid:pk>/update/', VideoURLUpdateView.as_view(), name='video-update'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
]
