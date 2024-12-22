from django.contrib import admin

from .models import UserRequest


@admin.register(UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "phone_number"]
    list_display_links = ["pk", "name"]
