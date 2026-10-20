from django.db import models
from django.utils.text import slugify
from encyclopedia.models import Person


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Category Name',
    )

    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
        verbose_name='URL Slug',
    )

    description = models.TextField(
        blank=True,
        verbose_name='Description',
    )

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(f"{self.name}")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category',
        verbose_name_plural = 'Categories'


class Work(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Title',
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        verbose_name='URL Slug',
    )

    person = models.ForeignKey(
        to=Person,
        on_delete=models.CASCADE,
        related_name='works',
        verbose_name='Creator',
    )

    categories = models.ManyToManyField(
        to=Category,
        related_name='works',
        blank=True,
        verbose_name='Categories',
    )

    year_created = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Year Created',
    )

    description = models.TextField(
        verbose_name='Description',
    )

    image = models.ImageField(
        upload_to='works/',
        null=True,
        blank=True,
        verbose_name='Image',
    )

    is_masterpiece = models.BooleanField(
        default=False,
        verbose_name='Is Masterpiece',
    )

    def __str__(self) -> str:
        return f"{self.title} by {self.person}"

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(f"{self.title}")
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-is_masterpiece', 'title']
        verbose_name = 'Work'
        verbose_name_plural = 'Works'