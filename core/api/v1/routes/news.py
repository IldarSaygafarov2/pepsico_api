from ninja import Router
from core.api.core.schemas.news import NewsSchema, NewsDetailSchema
from core.api.core.services.news import news_service

router = Router(tags=["News"])


@router.get("/", response=list[NewsSchema])
def get_news(request):
    return news_service.get_news()


@router.get("/{pk}", response=NewsDetailSchema)
def get_news_detail(request, pk):
    return news_service.get_news_detail(pk)
