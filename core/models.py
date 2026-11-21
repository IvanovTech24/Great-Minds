from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify


class SluggedModelMixin(models.Model):
    slug_source_field = None
    
    class Meta:
        abstract = True
        
    def _build_slug(self) -> str:
        if not self.slug_source_field:
            raise NotImplementedError(
                f"{self.__class__.__name__} must define 'slug_source_field'."
            )
        source_value = getattr(self, self.slug_source_field)
        return slugify(source_value)
    
    def clean(self):
        super().clean()
        if not self.slug:
            self.slug = self._build_slug()
            
        qs = self.__class__.objects.filter(slug=self.slug)
        if self.pk:
            qs = qs.exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError(
                {"slug": "An object with this slug already exists."
                         "Please choose a different name/title."}
            )
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
