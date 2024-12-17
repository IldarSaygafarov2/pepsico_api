from datetime import date
from typing import Optional, List

from ninja import Schema


class NewsHeadlinerSchema(Schema):
    id: int
    text: str


class NewsImageSchema(Schema):
    id: int
    image: str


class NewsSchema(Schema):
    id: int
    title: str
    short_description: str
    image: str
    published_date: date
    headliners: Optional[List[NewsHeadlinerSchema]]


class NewsDetailSchema(Schema):
    id: int
    title: str
    full_description: str
    image: str
    published_date: date
    images: Optional[List[NewsImageSchema]]
