from django.shortcuts import render, redirect
from .forms import CreateBrandForm
from django.contrib import messages
from .models import Brand
from django.http import Http404

def createBrand(request):
    if request.method == "GET":
        brand_form = CreateBrandForm()
    else:
        brand_form = CreateBrandForm(request.POST)

        if brand_form.is_valid():
            brand_form.save()
            messages.success(request , "new brand added successfully")
        
        return redirect("new-brand")

    context = {
        "form": brand_form
    }
    return render(request, "new-brand.html", context)


def getBrands(request):
    brandQueryParam = request.GET.get("brand")
    regionQueryParam = request.GET.get("region")


    print(brandQueryParam, regionQueryParam)
    
    
    brands = Brand.objects.all()

    if brandQueryParam is not None:
        brands = brands.filter(name__iexact=brandQueryParam)
    if regionQueryParam is not None:
        brands = brands.filter(region__icontains=regionQueryParam)

    
    if brands.count() < 1:
        raise Http404 


    context = {"brands": brands}


    return render(request , "brands.html", context)
    