from django.contrib import admin

from .models import MissionAndValue



@admin.register(MissionAndValue)
class MissionAndValueAdmin(admin.ModelAdmin):
    pass
