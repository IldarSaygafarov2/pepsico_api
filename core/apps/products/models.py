from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.categories.models import Category


class Product(TimedBaseModel):
    name = models.CharField(verbose_name="Название", max_length=150)
    size = models.IntegerField(
        default=500,
        verbose_name="Объем",
        help_text="Указывается объем продукта для отображения на главной странице",
    )
    image = models.ImageField(verbose_name="Фото", upload_to="products/images/")
    about_product = models.TextField(verbose_name="Об этом продукте")
    description = models.TextField(verbose_name="Описание")
    about_brand = models.TextField(verbose_name="О бредне")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="categories",
    )

    def __str__(self):
        return f"{self.name} - {self.size}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductSize(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name="Продукт",
        on_delete=models.CASCADE,
        related_name="sizes",
    )
    size = models.FloatField(verbose_name="Объем")
