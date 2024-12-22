from core.apps.categories.models import Category
from core.apps.products.models import Product
from django.shortcuts import get_object_or_404


class ProductService:
    def get_products_with_categories(self):
        categories = Category.objects.all()
        result = []

        for category in categories:
            result.append(
                {
                    "category": {
                        "id": category.pk,
                        "name": category.name,
                        "banner_image": (
                            category.banner_image.url if category.banner_image else ""
                        ),
                    },
                    "products": [],
                }
            )

        for category in result:
            category_name = category.get("category").get("name")
            products = Product.objects.filter(category__name=category_name)
            for product in products:
                category["products"].append(
                    {
                        "id": product.pk,
                        "name": product.name,
                        "image": product.image.url if product.image else "",
                        "size": product.size,
                    }
                )
        return result

    def get_product_detail(self, product_id: int):
        product = get_object_or_404(Product, pk=product_id)
        return product

    def get_all_products(self):
        return Product.objects.all()


product_service = ProductService()
