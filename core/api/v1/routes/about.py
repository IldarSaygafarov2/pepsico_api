from ninja import Router
from django.http import HttpRequest
from core.api.core.schemas.about import MissionAndValueSchema, PhotoGallerySchema
from core.api.core.services.about import about_service

router = Router(tags=["About"])


@router.get("/missions_and_values", response=list[MissionAndValueSchema])
def get_about(request: HttpRequest):
    return about_service.get_missions_and_values()


@router.get("/photo-gallery", response=list[PhotoGallerySchema])
def get_photo_gallery(request):
    return about_service.get_photos_gallery()
