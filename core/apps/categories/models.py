from django.db import models

from core.apps.common.models import TimedBaseModel


class Category(TimedBaseModel):
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)
    banner_image = models.ImageField(upload_to='categories/banners/',
                                     verbose_name='Фото заднего фона',
                                     null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-created_at']
