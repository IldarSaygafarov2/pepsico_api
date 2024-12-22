from django.db import models


class UserRequest(models.Model):
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")
    name = models.CharField(max_length=100, verbose_name="Имя")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name}-{self.phone_number}"

    class Meta:
        verbose_name = "Заявка пользователя"
        verbose_name_plural = "Заявки пользователей"
