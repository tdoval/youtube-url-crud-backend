from rest_framework import serializers
from urls.infrastructure.models import VideoURL
from django.contrib.auth.models import User

class VideoURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoURL
        fields = ['id', 'url', 'added_at']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
