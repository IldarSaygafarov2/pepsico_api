from modeltranslation.translator import register, TranslationOptions
from .models import MissionAndValue


@register(MissionAndValue)
class MissionAndValueTranslationOptions(TranslationOptions):
    fields = ("name", "description")
