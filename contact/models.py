from django.db import models


class Contact(models.Model):
    """Модель контактной формы"""
    name = models.CharField("ФИО", max_length=100)
    email = models.EmailField("Email", max_length=100, unique=True)
    subject = models.CharField("Тема обращения", max_length=30)
    message = models.TextField("Текст обращения")

    class Meta:
        verbose_name = "Контакная форма"
        verbose_name_plural = "Контакные формы"
        ordering = ["name"]

    def __str__(self):
        return self.name