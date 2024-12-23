from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import MissionAndValue


@admin.register(MissionAndValue)
class MissionAndValueAdmin(TranslationAdmin):
    pass
