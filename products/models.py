from django.db import models
from brands.models import Brand
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator


class Phone(models.Model):
    # model name
    model       = models.CharField(max_length=256 , unique=True)
    # brand foreign key
    brand       = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color       = models.CharField(max_length=128)
    # validators is for validating if number is positive or not
    screen_size = models.DecimalField(
        verbose_name="screen size (inch)", 
        max_digits=3, 
        decimal_places=2, 
        validators=[MinValueValidator(0.0)])
    
    price       = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        validators=[MinValueValidator(0.0)])
    # country field imported from django_countries package
    region          = CountryField()
    is_available    = models.BooleanField(default=True, blank=True, verbose_name="is available")
    # number of products available
    count           = models.IntegerField(validators=[MinValueValidator(0)])

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)



    def __str__(self) -> str:
        return self.model
    # checks if a record's brand region is same as their phone region
    def isSameRegion(self) -> bool: 
        return self.region == self.brand.region
    