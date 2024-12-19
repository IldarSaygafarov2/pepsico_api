from django.db import models

from core.apps.common.models import TimedBaseModel


class Category(TimedBaseModel):
    name = models.CharField(max_length=100, verbose_name="Название", unique=True)
    banner_image = models.ImageField(
        upload_to="categories/banners/",
        verbose_name="Фото заднего фона",
        null=True,
        blank=True,
        help_text="Фотография фона на странице всей продукции",
    )
    product_image = models.ImageField(
        verbose_name="Фотография продукта категории",
        upload_to="categories/products/",
        null=True,
        blank=True,
        help_text="Фотография продукта данной категории на главной странице",
    )
    description = models.TextField(
        verbose_name="Описание для категории",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["-created_at"]
