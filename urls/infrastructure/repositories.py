from urls.infrastructure.models import VideoURL

class VideoURLRepository:

    @staticmethod
    def get_all_videos():
        return VideoURL.objects.all()

    @staticmethod
    def create_url(url, user):
        return VideoURL.objects.create(url=url, user=user, name=None)

    @staticmethod
    def get_user_videos(user):
        return VideoURL.objects.filter(user=user, deleted_at__isnull=True).order_by('-added_at')

    @staticmethod
    def get_video_by_id(video_id):
        return VideoURL.objects.filter(id=video_id, deleted_at__isnull=True).first()

    @staticmethod
    def delete_video(video_id):
        video = VideoURLRepository.get_video_by_id(video_id)
        if video:
            video.soft_delete()
