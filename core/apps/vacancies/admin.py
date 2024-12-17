from django.contrib import admin

from .models import Vacancy, VacancyRequirement, VacancyCondition, VacancyResponsibility


class VacancyResponsibilityInline(admin.StackedInline):
    model = VacancyResponsibility
    extra = 1


class VacancyConditionInline(admin.StackedInline):
    model = VacancyCondition
    extra = 1


class VacancyRequirementInline(admin.StackedInline):
    model = VacancyRequirement
    extra = 1


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    inlines = [
        VacancyResponsibilityInline,
        VacancyConditionInline,
        VacancyRequirementInline,
    ]
