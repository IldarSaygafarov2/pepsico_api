from ninja import Router


router = Router(
    tags=['Products']
)

@router.get('/')
def get_products(request):
    return []