from ninja import Router
from core.apps.about.models import MissionAndValue
from core.api.core.schemas.about import MissionAndValueSchema

router = Router(
    tags=['About']
)


@router.get('/missions_and_values', response=list[MissionAndValueSchema])
def get_about(request):
    items = MissionAndValue.objects.all()
    return items
