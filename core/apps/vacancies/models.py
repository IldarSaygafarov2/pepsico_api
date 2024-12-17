from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    photo = models.ImageField(upload_to='vacancies/images/', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class VacancyResponsibility(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='responsibilities')
    title = models.CharField(max_length=255, verbose_name='текст')

    def __str__(self):
        return self.title


class VacancyRequirement(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='requirements')
    title = models.CharField(max_length=255, verbose_name='текст')

    def __str__(self):
        return self.title


class VacancyCondition(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='conditions')
    title = models.CharField(max_length=255, verbose_name='текст')

    def __str__(self):
        return self.title
