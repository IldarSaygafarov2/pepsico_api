from django.shortcuts import get_object_or_404
from core.apps.news.models import News


class NewsService:
    def get_news(self) -> list[News]:
        return News.objects.all()

    def get_news_detail(self, news_id: int) -> News:
        return get_object_or_404(News, pk=news_id)


news_service = NewsService()
