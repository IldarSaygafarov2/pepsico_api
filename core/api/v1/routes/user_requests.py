from ninja import Router
from django.http import HttpRequest
from core.apps.user_requests.models import UserRequest

from core.api.core.schemas.user_request import UserRequestInSchema, UserRequestOutSchema


router = Router(
    tags=["User requests"],
)


@router.post("/create", response=UserRequestOutSchema)
def create_user_request(request: HttpRequest, data: UserRequestInSchema):
    new_request = UserRequest.objects.create(**data.model_dump())
    return new_request
