from django.urls import path
from . import views

urlpatterns = [
    path("new", views.createBrand , name="new-brand"),
    path("" , views.getBrands, name="get-brands")
]