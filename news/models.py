from django.db import models
from django.contrib.auth.models import User

# from .forms import CommentForm
from django.urls import reverse
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey
from photologue.models import Gallery


class Category(MPTTModel):
    """Модель категорий для статей"""
    name = models.CharField("Название категория", max_length=150)
    slug = models.SlugField("url", unique=True)
    template_name = models.CharField("Название шаблона", max_length=100, default="news/post-list.html")
    pagination = models.PositiveSmallIntegerField("Количество статей на страницу", default=10)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse('post_by_category_url', kwargs={"category": self.slug})


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
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор статьи",
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    title = models.CharField("Название статьи", max_length=250)
    sub_title = models.CharField("Подзаголовок", max_length=150, blank=False)
    slug = models.SlugField("url", max_length=250, unique=True, blank=False)
    text = models.TextField("Текст статьи")
    image = models.ImageField("Картинка статьи", upload_to="post/", blank=True)
    gallery = models.ForeignKey(Gallery, verbose_name="Галерея", blank=True, null=True, on_delete=models.SET_NULL)
    is_private = models.BooleanField("Отображение для всех", default=True, null=True)
    template_name = models.CharField("Шаблон статьи", max_length=200, default="news/post-detail.html", blank=False)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    updated = models.DateTimeField(
        "Дата обновления статьи",
        default=timezone.now,
        blank=True,
        null=True
    )
    pub_date = models.DateTimeField(
        "Дата публикации",
        default=timezone.now,
        blank=False,
        null=True
    )
    published = models.BooleanField("Опубликовать?", default=True, blank=False)

    def __str__(self):
        return self.title

    def get_comments(self):
        return Comment.objects.filter(post__slug=self.slug)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={"category": self.category.slug, "slug": self.slug})

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-pub_date"]


class Comment(MPTTModel):
    """Модель комментариев к статье"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        null=True
    )
    post = models.ForeignKey(
        Post,
        verbose_name="Статья",
        on_delete=models.CASCADE
    )
    text = models.TextField("Комментарий")
    moderation = models.BooleanField("Разрешено к публикации", default=False, null=True)
    created = models.DateTimeField("Дата написания", auto_now_add=True, null=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return "{}".format(self.post.title)

    class MPTTMeta:
        level_attr = 'mptt_level'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created"]