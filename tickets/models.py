from django.db import models

# Create your models here.
from django.urls import reverse


class Ticket(models.Model):
    """модель тикетов в тех.поддержку"""
    user = models.CharField("Пользователь", max_length=150)
    room = models.PositiveIntegerField("Кабинет")
    title = models.CharField("Название", max_length=200)
    text = models.TextField("Текст обрашения")
    created = models.DateTimeField("Дата сообщения", auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tickets_list_url')

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ['-created']