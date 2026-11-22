from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from encyclopedia.models import Person
from core.models import SluggedModelMixin
from .managers import CustomUserManager



class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name='Email Address',
        error_messages={
            'unique': "A user with that email already exists.",
        }
    )

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.username


class Profile(SluggedModelMixin ,models.Model):
    slug_source_field = None

    user = models.OneToOneField(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Biography',
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True,
        verbose_name='Avatar',
    )
    slug = models.SlugField(
        max_length=150,
        unique=True,
        blank=True,
    )

    def _build_slug(self) -> str:
        return slugify(self.user.username)

    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"


class Favorite(models.Model):
    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
    )
    person = models.ForeignKey(
        to=Person,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'person'],
                name='unique_user_person_favorite',
            )
        ]
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'

    def __str__(self) -> str:
        return f"{self.user.username} favorites {self.person}"