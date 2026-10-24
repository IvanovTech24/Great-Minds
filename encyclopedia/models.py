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
        verbose_name='Era Color',
        help_text='Pick a color that represents this era.'
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


class Quote(models.Model):
    text = models.TextField(
        verbose_name='Quote Text',
    )

    person = models.ForeignKey(
        to=Person,
        on_delete=models.CASCADE,
        related_name='quotes',
        verbose_name='Person',
    )

    source = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Source (e.g. Book, Speech)'
    )

    def __str__(self) -> str:
        if len(self.text) > 50:
            return f'"{self.text[:50]}..."'
        return f'"{self.text}"'

    class Meta:
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'


class Influence(models.Model):
    influencer = models.ForeignKey(
        to=Person,
        on_delete=models.CASCADE,
        related_name='influenced',
        verbose_name='Influencer (The one who inspires)',
    )

    influenced = models.ForeignKey(
        to=Person,
        on_delete=models.CASCADE,
        related_name='influenced_by',
        verbose_name='Influenced (The one who was inspired)',
    )

    description = models.TextField(
        blank=True,
        verbose_name='Description of influence',
    )

    def __str__(self) -> str:
        return f"{self.influencer} -> {self.influenced}"

    class Meta:
        unique_together = ('influencer', 'influenced')
        verbose_name = 'Influence'
        verbose_name_plural = 'Influences'