from ninja import Router

router = Router(
    tags=['About']
)

@router.get('/')
def get_about(request):
    return []
