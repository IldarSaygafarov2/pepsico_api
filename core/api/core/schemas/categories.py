from typing import Optional
from ninja import Schema


class CategoryOut(Schema):
    id: int
    name: str
    banner_image: Optional[str] = None


class HomePageCategorySchema(Schema):
    id: int
    name: str
    description: Optional[str]
    product_image: Optional[str]
