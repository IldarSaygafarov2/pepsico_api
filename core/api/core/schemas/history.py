from ninja import Schema


class BrandHistoryImageSchema(Schema):
    id: int
    image: str


class BrandHistorySchema(Schema):
    id: int
    title: str
    year: int
    images: list[BrandHistoryImageSchema]
