from ninja import Router
from django.shortcuts import get_object_or_404
from core.apps.news.models import News
from core.api.core.schemas.news import NewsSchema, NewsDetailSchema

router = Router(
    tags=['News']
)


@router.get('/', response=list[NewsSchema])
def get_news(request):
    news = News.objects.all()
    return news


@router.get('/{pk}', response=NewsDetailSchema)
def get_news_detail(request, pk):

    news_item = get_object_or_404(News, pk=pk)
    return news_item