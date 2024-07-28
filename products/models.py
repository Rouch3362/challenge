from django.db import models
from brands.models import Brand
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator


class Phone(models.Model):
    model       = models.CharField(max_length=256 , unique=True)
    brand       = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color       = models.CharField(max_length=128)
    screen_size = models.DecimalField(
        verbose_name="screen size (inch)", 
        max_digits=3, 
        decimal_places=2, 
        validators=[MinValueValidator(0.0)])
    
    price       = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        validators=[MinValueValidator(0.0)])
    
    region      = CountryField()
    status      = models.BooleanField(default=True, blank=True)
    count       = models.IntegerField()

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)



    def __str__(self) -> str:
        return self.model
    