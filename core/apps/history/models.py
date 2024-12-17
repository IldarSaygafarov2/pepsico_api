from django.db import models

# Create your models here.


class BrandHistory(models.Model):
    year = models.IntegerField(verbose_name="год")
    title = models.CharField(verbose_name="заголовок", max_length=100)

    def __str__(self):
        return f"{self.year} - {self.title}"

    class Meta:
        verbose_name = "История бренда"
        verbose_name_plural = "История бренда"


class BrandHistoryImage(models.Model):
    brand_history = models.ForeignKey(BrandHistory, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='history/images')

