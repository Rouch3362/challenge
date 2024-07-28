from django.shortcuts import render, redirect
from .forms import CreatePhone
from django.contrib import messages
from .models import Phone
from django.http import Http404
from django.db.models import Q


def createPhoneObj(request):
    if request.method == "GET":
        # an empty instance of form
        phone_form = CreatePhone()

    else:
        phone_form = CreatePhone(request.POST)
        # validating form's data
        if phone_form.is_valid():
            phone_form.save()
            # showing user their action was successfull
            messages.success(request , "new phone added successfully")
            return redirect("new-phone")
    
    context = {
        "form": phone_form
    }

    return render(request , "new-phone.html", context)



def getPhones(request):
    # getting optional query parameters
    brandQueryParam = request.GET.get("brand")
    regionQueryParam = request.GET.get("region")
    # is for filtering the products that their region is same as their brand region
    isSameRegion = request.GET.get("same-region")
    # getting all objects in database
    phones = Phone.objects.all()

    # filtering base on query parameters entered by user
    if brandQueryParam is not None:
        phones = phones.filter(brand__name__iexact=brandQueryParam)
    if regionQueryParam is not None:
        phones = phones.filter(region__icontains=regionQueryParam)
    if isSameRegion == "true":   
        # checking for if they are hase same region in brand and phone using phone model method
        phones = [phone for phone in phones if phone.isSameRegion()]


    # check if filtering result is empty or not
    if len(phones) < 1:
        raise Http404 


    context = {"phones": phones}


    return render(request , "phones.html", context)
    