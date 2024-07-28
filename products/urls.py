from django.urls import path
from . import views

urlpatterns = [
    path("new/", views.createPhoneObj , name="new-phone"),
    path("", views.getPhones , name="phones")
]



