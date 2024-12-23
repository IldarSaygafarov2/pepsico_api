from django.contrib import admin

from .models import BrandHistoryImage, BrandHistory, PhotoGallery
from modeltranslation.admin import TranslationAdmin


class BrandHistoryImageInline(admin.StackedInline):
    model = BrandHistoryImage
    extra = 1


@admin.register(BrandHistory)
class BrandHistoryAdmin(TranslationAdmin):
    inlines = [BrandHistoryImageInline]


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    pass
