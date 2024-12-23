from core.apps.categories.models import Category


class CategoryService:
    def get_categories(self):
        categories = Category.objects.all()
        return categories


category_service = CategoryService()
