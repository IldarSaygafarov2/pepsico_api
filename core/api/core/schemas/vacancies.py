from typing import Optional

from ninja import Schema


class VacancyResponsibilitySchema(Schema):
    id: int
    title: str


class VacancyConditionSchema(Schema):
    id: int
    title: str


class VacancyRequirementSchema(Schema):
    id: int
    title: str


class VacancySchema(Schema):
    id: int
    title: str
    photo: str
    responsibilities: Optional[list[VacancyResponsibilitySchema]]
    requirements: Optional[list[VacancyRequirementSchema]]
    conditions: Optional[list[VacancyConditionSchema]]
