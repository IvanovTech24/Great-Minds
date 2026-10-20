from django.db import models
from django.utils.text import slugify


class Era(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Era Name',
    )
    start_year = models.IntegerField(
        verbose_name='Start Year',
    )

    end_year = models.IntegerField(
        verbose_name='End Year',
    )

    description = models.TextField(
        verbose_name='Description'
    )

    color_hex = models.CharField(
        max_length=7,
        default='#6c757d',
        verbose_name='Color (Hex Code)',
        help_text='Enter a hex color code (e.g., #FF5733)'
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['start_year']
        verbose_name = 'Era'
        verbose_name_plural = 'Eras'


class Person(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name='Last Name',

    )
    birth_year = models.IntegerField(
        verbose_name='Birth Year'
    )

    death_year = models.IntegerField(
        verbose_name='Death Year',
        null=True,
        blank=True,
    )

    nationality = models.CharField(
        max_length=100,
        verbose_name='Nationality',
    )

    short_bio = models.CharField(
        max_length=300,
        verbose_name='Short Biography',
        help_text='A brief summary (max 300 characters)',
    )

    biography = models.TextField(
        verbose_name='Full Biography',
    )

    fun_fact = models.TextField(
        verbose_name='Fun Fact',
        blank=True,
        help_text='A curious or lesser-known fact about this person'
    )

    portrait = models.ImageField(
        verbose_name='Portrait Image',
        upload_to='portraits/',
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        max_length=150,
        unique=True,
        blank=True,
        verbose_name='URL Slug',
    )

    era = models.ForeignKey(
        to=Era,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Historical Era',
        related_name='people'
    )


    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}")
        super().save(*args, **kwargs)


    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Person'
        verbose_name_plural = 'People'