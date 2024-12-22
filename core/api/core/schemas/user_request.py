from datetime import datetime
from ninja import Schema


class UserRequestInSchema(Schema):
    phone_number: str
    name: str


class UserRequestOutSchema(Schema):
    id: int
    phone_number: str
    name: str
    created_at: datetime
