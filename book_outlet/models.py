from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_best_selling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True) # NEW
    
    def get_absolute_url(self) -> str:
        return reverse('book-detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) # Esto crea un slug a partir del title antes de que se guarde (abajo).
        super().save( *args, **kwargs) # Esto es para mantener los save methods que ya tenemos. 
    
    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"
