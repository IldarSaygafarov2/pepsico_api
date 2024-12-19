from ninja import Router
from core.apps.products.models import Product
from core.api.core.schemas.products import ProductListSchema, ProductShortSchema


router = Router(tags=["Products"])


@router.get("/", response=ProductListSchema)
def get_products(request):
    products = Product.objects.all()
    result = ProductListSchema(products=products)
    return result


@router.get("/{product_id}")
def get_product(request, product_id: int):
    return {}
