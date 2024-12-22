from ninja import Router
from core.api.core.schemas.categories import HomePageCategorySchema
from core.api.core.schemas.products import ProductDetailSchema
from core.api.core.services.categories import category_service
from core.api.core.services.products import product_service

router = Router(
    tags=["Homepage"],
)


@router.get("/categories", response=list[HomePageCategorySchema])
def get_home_categories(request):
    return category_service.get_categories()


@router.get("/products", response=list[ProductDetailSchema])
def get_home_products(request):
    return product_service.get_all_products()
