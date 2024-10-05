from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from urls.infrastructure.models import VideoURL
from urls.interfaces.serializers import VideoURLSerializer
from urls.interfaces.serializers import UserRegistrationSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class VideoURLListCreateView(generics.ListCreateAPIView):
    queryset = VideoURL.objects.all().order_by('-added_at')
    serializer_class = VideoURLSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VideoURLDeleteView(generics.DestroyAPIView):
    queryset = VideoURL.objects.all()
    serializer_class = VideoURLSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
