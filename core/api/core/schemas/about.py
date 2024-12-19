from ninja import Schema


class MissionAndValueSchema(Schema):
    id: int
    name: str
    description: str


class PhotoGallerySchema(Schema):
    id: int
    image: str
