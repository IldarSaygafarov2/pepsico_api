from django.contrib import admin

from .models import BrandHistoryImage, BrandHistory, PhotoGallery


class BrandHistoryImageInline(admin.StackedInline):
    model = BrandHistoryImage
    extra = 1


@admin.register(BrandHistory)
class BrandHistoryAdmin(admin.ModelAdmin):
    inlines = [BrandHistoryImageInline]


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    pass
