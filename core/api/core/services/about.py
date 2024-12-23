from core.apps.about.models import MissionAndValue
from core.apps.history.models import PhotoGallery


class AboutService:
    def get_missions_and_values(self):
        objects = MissionAndValue.objects.all()
        return objects

    def get_photos_gallery(self):
        gallery = PhotoGallery.objects.all()
        return gallery


about_service = AboutService()
