from ninja import Router

router = Router(
    tags=['Vacancies']
)

@router.get('/')
def get_vacancies(request):
    return []
