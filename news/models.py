from django.db import models
from django.http import request

# from .forms import CommentForm


class Category(models.Model):
    """Модель категорий для статей"""
    name = models.CharField("Название категория", max_length=150)
    slug = models.SlugField("url", unique=True)
    template_name = models.CharField("Название шаблона", max_length=100, default="news/post-list.html")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Tag(models.Model):
    """Модель тегов статей"""
    name = models.CharField("Название тега", max_length=100)
    slug = models.SlugField("url", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["name"]


class Post(models.Model):
    """Модель статьи"""
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null=True
    ) #при удалении категории поле "категория" в статье будет задана как "null"
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        verbose_name="Автор статьи",
        blank=True
    )
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    title = models.CharField("Название статьи", max_length=250)
    sub_title = models.CharField("Подзаголовок", max_length=150, blank=False)
    slug = models.SlugField("url", max_length=250, unique=True, blank=False)
    text = models.TextField("Текст статьи")
    is_private = models.BooleanField("Отображение для всех", default=True, null=True)
    template_name = models.CharField("Шаблон статьи", max_length=200, default="news/post-detail.html", blank=False)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    updated = models.DateTimeField("Дата обновления статьи", auto_now_add=True, auto_now=False)
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True, blank=False)
    published = models.BooleanField("Опубликовано", default=True, blank=False)

    def __str__(self):
        return self.title

    def get_comments(self):
        return Comment.objects.filter(post__slug=self.slug)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-pub_date"]


class Comment(models.Model):
    """Модель комментариев к статье"""
    post = models.ForeignKey(
        Post,
        verbose_name="Статья",
        on_delete=models.CASCADE
    ) #при удалении статьи комментарии будут удаляться
    text = models.TextField("Комментарий")
    moderation = models.BooleanField("Разрешено к публикации", default=False)
    created = models.DateTimeField("Дата написания", auto_now_add=True)

    def __str__(self):
        return "{}".format(self.post.title)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created"]