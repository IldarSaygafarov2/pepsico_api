from django.db import models


class MissionAndValue(models.Model):
    name = models.CharField(max_length=150, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Миссия и ценность"
        verbose_name_plural = "Миссия и ценности"
