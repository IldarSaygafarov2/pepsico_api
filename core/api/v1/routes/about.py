from ninja import Router
from core.apps.about.models import MissionAndValue
from core.apps.history.models import PhotoGallery
from core.api.core.schemas.about import MissionAndValueSchema, PhotoGallerySchema

router = Router(tags=["About"])


@router.get("/missions_and_values", response=list[MissionAndValueSchema])
def get_about(request):
    items = MissionAndValue.objects.all()
    return items


@router.get("/photo-gallery", response=list[PhotoGallerySchema])
def get_photo_gallery(request):
    items = PhotoGallery.objects.all()
    return items
