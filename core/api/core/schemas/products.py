from typing import Optional
from ninja import Schema
from core.api.core.schemas.categories import CategoryOut


class ProductShortSchema(Schema):
    id: int
    name: str
    size: int
    image: str


class ProductListSchema(Schema):
    # category: CategoryOut
    products: list[ProductShortSchema]
