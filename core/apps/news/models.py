from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    short_description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Полное описание')
    image = models.ImageField(upload_to="news/", verbose_name='Фото')
    published_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class NewsHeadliner(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='headliners')
    text = models.TextField()


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="news/")

