from typing import Optional
from ninja import Schema


class CategoryOut(Schema):
    id: int
    name: str
    image: Optional[str] = None

