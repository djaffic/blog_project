from django.db import models


class Contact(models.Model):
    """Модель контактной формы"""
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    email = models.EmailField("Email", max_length=100, unique=True)
    message = models.TextField("Текст обращения")

    class Meta:
        verbose_name = "Контакная форма"
        verbose_name_plural = "Контакные формы"
        ordering = ["-last_name"]

    def __str__(self):
        return "{}-{}".format(self.last_name, self.first_name)