from typing import Optional
from ninja import Schema
from core.api.core.schemas.categories import CategoryOut


class ProductShortSchema(Schema):
    id: int
    name: str
    size: int
    image: str


class ProductListSchema(Schema):
    category: CategoryOut
    products: list[ProductShortSchema]


class ProductSizeSchema(Schema):
    id: int
    size: float


class ProductDetailSchema(Schema):
    id: int
    name: str
    about_product: str
    about_brand: str
    image: str
    description: Optional[str]
    category: CategoryOut
    sizes: Optional[list[ProductSizeSchema]]
