from ninja import Router

from core.api.core.schemas.vacancies import VacancySchema
from core.apps.vacancies.models import Vacancy

router = Router(
    tags=['Vacancies']
)


@router.get('/', response=list[VacancySchema])
def get_vacancies(request):
    items = Vacancy.objects.all()
    return items
