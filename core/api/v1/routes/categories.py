from ninja import Router
from core.apps.categories.models import Category
from core.api.core.schemas.categories import CategoryOut, HomePageCategorySchema

router = Router(tags=["Categories"])


@router.get("/")
def get_categories(request):
    return []


@router.get("/homepage", response=list[HomePageCategorySchema])
def get_categories_for_home_page(request):
    categories = Category.objects.all()
    return categories
