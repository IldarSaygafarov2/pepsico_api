from ninja import Router
from core.apps.history.models import BrandHistory
from core.api.core.schemas.history import BrandHistorySchema

router = Router(
    tags=['History']
)


@router.get('/brand', response=list[BrandHistorySchema])
def get_history(request):
    items = BrandHistory.objects.all()
    return items
    