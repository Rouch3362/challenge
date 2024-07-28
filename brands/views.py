from django.shortcuts import render, redirect
from .forms import CreateBrandForm
from django.contrib import messages
from .models import Brand
from django.http import Http404

def createBrand(request):
    # if request is a get request
    if request.method == "GET":
        # a empty instance of form
        brand_form = CreateBrandForm()
    else:
        brand_form = CreateBrandForm(request.POST)
        # check if form data is valid
        if brand_form.is_valid():
            brand_form.save()
            # showing a message to user that the record created
            messages.success(request , "new brand added successfully")
            return redirect("new-brand")
    
        

    context = {
        "form": brand_form
    }
    return render(request, "new-brand.html", context)


def getBrands(request):
    # getting query parameters
    brandQueryParam = request.GET.get("brand")
    regionQueryParam = request.GET.get("region")
    
    # getting all of brands and filtering them based on query parameters
    brands = Brand.objects.all()

    if brandQueryParam is not None:
        # filter them based on brand name without considering if it is uppercase or not 
        brands = brands.filter(name__iexact=brandQueryParam)
    if regionQueryParam is not None:
        # filtering base on region
        brands = brands.filter(region__icontains=regionQueryParam)

    # if filtering result comes empty
    if brands.count() < 1:
        raise Http404 


    context = {"brands": brands}


    return render(request , "brands.html", context)
    