from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from urls.infrastructure.models import VideoURL
from urls.infrastructure.repositories import VideoURLRepository
from urls.interfaces.serializers import VideoURLSerializer, UserRegistrationSerializer
from urls.permissions.permissions import IsOwner

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class VideoURLListCreateView(generics.ListCreateAPIView):
    serializer_class = VideoURLSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return VideoURLRepository.get_user_videos(self.request.user)

    def perform_create(self, serializer):
        VideoURLRepository.create_url(serializer.validated_data['url'], self.request.user)

class VideoURLUpdateView(generics.UpdateAPIView):
    queryset = VideoURL.objects.all()
    serializer_class = VideoURLSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

class VideoURLDeleteView(generics.DestroyAPIView):
    queryset = VideoURL.objects.all()
    serializer_class = VideoURLSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            raise PermissionDenied("Você não tem permissão para deletar este vídeo.")
        
        VideoURLRepository.delete_video(instance.id)
        
        return Response(status=status.HTTP_204_NO_CONTENT)