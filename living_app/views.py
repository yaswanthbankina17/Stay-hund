from django.shortcuts import render
from living_app.models import property,property_details,property_interior_img
# Create your views here.


def index(request):
    types=list(property.objects.values_list("property_type",flat=True).distinct())
    print(types)
    return render(request,"index.html",{"types":types})



def pg_view(request):
    pg_list=property.objects.filter(property_type="PG")

    pg_name=request.GET.get("pg_name","")
    location=request.GET.get("location","")
    location_names=pg_list.values_list("location",flat=True).distinct()
    res="No PG Found"
    if pg_name:
        pg_list=pg_list.filter(name__icontains=pg_name)  # icontains means that pg name is matches pg list it will redirect like:- pg_list=[ravi,ramesh] if you search ra it will give matching pg's
    if location:
        pg_list=pg_list.filter(location__icontains=location)
    context={
        "pg_list":pg_list,
        "res":res,
        "pg_name":pg_name,
        "location":location,
        "loc_names":location_names
    }
    return render(request, "pg.html",context)

def pg_inte_view(request,id):
    property_name=property.objects.get(id=id)
    property_lnfo=property_details.objects.get(property_de__id=id)
    property_images=property_interior_img.objects.filter(property_interior__id=id)
    context={
        "property_name":property_name,
        "property_info":property_lnfo,
        "property_images":property_images
    }
    return render(request, "details.html",context)


def coliv_view(request):
    coliv_list=property.objects.filter(property_type="coliving")
    location_names=coliv_list.values_list("location",flat=True).distinct()
    coliv_name=request.GET.get("coliv_name","")
    location=request.GET.get("location","")

    if coliv_name:
        coliv_list=coliv_list.filter(name__icontains=coliv_name)
    if location:
        coliv_list=coliv_list.filter(location__icontains=location)
    context={
        "coliv_list":coliv_list,
        "location_names":location_names,
        "coliv_name":coliv_name,
        "location":location
    }
    return render(request,"coliv.html",context)

def coliv_inte_view(request,id):
    property_name=property.objects.get(id=id)
    property_inte_images=property_interior_img.objects.filter(property_interior__id=id)
    property_info=property_details.objects.get(property_de__id=id)
    context={
        "property_name":property_name,
        "property_inte_images":property_inte_images,
        "property_info":property_info
    }
    return render(request,"coliv_details.html",context)

def homes_view(request):
    homes_list=property.objects.filter(property_type="home")
    location_names=homes_list.values_list("location",flat=True).distinct()
    home_name=request.GET.get("home_name","")
    location=request.GET.get("location","")

    if home_name:
        homes_list=homes_list.filter(name__icontains=home_name)
    if location:
        homes_list=homes_list.filter(location__icontains=location)
    context={
        "homes_list":homes_list,
        "home_name":home_name,
        "location_names":location_names,
        "location":location
    }
    return render (request,"homes.html",context)

def home_inte_view(request,id):
    property_name=property.objects.get(id=id)
    property_inte_images=property_interior_img.objects.filter(property_interior__id=id)
    property_info=property_details.objects.get(property_de__id=id)

    context={
        "property_name":property_name,
        "property_inte_images":property_inte_images,
        "property_info":property_info
    }
    return render(request,"home_details.html",context)

