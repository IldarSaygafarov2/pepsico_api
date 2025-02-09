from ninja import Router
from django.http import HttpRequest
from core.api.core.schemas.history import BrandHistorySchema
from core.api.core.services.history import history_service

router = Router(tags=["History"])


@router.get("/brand", response=list[BrandHistorySchema])
def get_history(request: HttpRequest):
    result = history_service.get_history_items()
    return result
