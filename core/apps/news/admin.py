
from django.contrib import admin

from .models import News, NewsImage, NewsHeadliner


class NewsImageInline(admin.StackedInline):
    model = NewsImage
    extra = 1


class NewsHeadlinerInline(admin.StackedInline):
    model = NewsHeadliner
    extra = 1


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageInline, NewsHeadlinerInline]
