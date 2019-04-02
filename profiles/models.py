from django.contrib.auth.models import User
from django.db import models


def get_profile_image(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class UserProfile(models.Model):
    """Профиль пользователя"""
    GENDER_CHOICES = (
        ("Man", "Mужской"),
        ("Woman", "Женский")
    )

    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField("Возраст")
    gender = models.CharField("Пол", choices=GENDER_CHOICES, max_length=3)
    profile_image = models.ImageField("Аватарка", upload_to=get_profile_image, blank=True, null=True)


