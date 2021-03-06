from django.db import models
from django.urls import reverse


class Page(models.Model):
    """Модель статических странииц"""
    title = models.CharField("Заголовок страницы", max_length=500)
    content = models.TextField("Текст")
    created = models.DateTimeField("Дата публикации", auto_now_add=True)
    template = models.CharField("Шаблон страницы", max_length=500, default="pages/index.html")
    slug = models.SlugField(
        "URL",
        max_length=500,
        unique=True,
        default="",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.slug:
            return reverse('pages:page', kwargs={'page': self.slug})
        else:
            return reverse('pages:page')