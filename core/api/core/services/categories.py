from core.apps.categories.models import Category


class CategoryService:
    def get_categories(self):
        return Category.objects.all()


category_service = CategoryService()
