from ninja import Router

from core.api.core.schemas.products import (
    ProductListSchema,
    ProductShortSchema,
    ProductDetailSchema,
)
from core.api.core.services.products import product_service
from core.apps.categories.models import Category
from core.apps.products.models import Product

router = Router(tags=["Products"])


@router.get("/")
def get_products(request):
    result = product_service.get_products_with_categories()
    return result


@router.get("/{product_id}", response=ProductDetailSchema)
def get_product(request, product_id: int):
    return product_service.get_product_detail(product_id)
