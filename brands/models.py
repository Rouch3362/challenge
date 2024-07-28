from django.db import models
from django_countries.fields import CountryField

class Brand(models.Model):
    name    = models.CharField(max_length=256)
    region  = CountryField()

    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self) -> str:
        return self.name