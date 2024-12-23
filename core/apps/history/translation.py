from modeltranslation.translator import register, TranslationOptions

from .models import BrandHistory


@register(BrandHistory)
class BrandHistoryTranslationOptions(TranslationOptions):
    fields = ["title"]
