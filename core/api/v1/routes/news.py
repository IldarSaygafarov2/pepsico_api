from ninja import Router


router = Router(
    tags=['News']
)


@router.get('/')
def get_news(request):
    return []
