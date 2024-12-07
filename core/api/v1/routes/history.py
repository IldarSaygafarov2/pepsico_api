from ninja import Router


router = Router(
    tags=['History']
)


@router.get('/')
def get_history(request):
    return []
    