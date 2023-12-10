from django.shortcuts import render
import os, json, csv
from django.db.models import Q
from django.core.serializers import serialize
from .models import *
from .forms import *
from django.shortcuts import render, redirect




# Create your views here.


def index(request):

    provinces_allocated = province_allocation.objects.all()
    allocationForm = farms_allocationForm()

    maize_total = 0
    fertilizer_total = 0
    sorghum_total = 0 
    
    allocated = Newfarms.objects.filter(status = 'Allocated')
    allocated_count = allocated.count()
    not_allocated = Newfarms.objects.filter(status = 'Not Allocated')
    not_allocated_count = not_allocated.count()

    if request.method ==  "POST":
        allocationForm =  farms_allocationForm(request.POST)
        if allocationForm.is_valid():
            allocationForm.save()

            farm = request.POST.get("farms")
            maize = request.POST.get("maize")
            fertilizer = request.POST.get("fertilizer")
            sorghum = request.POST.get("sorghum")


            province = Newfarms.objects.get(gid=farm).province

            selected_province = province_allocation.objects.get(province__name = province)

            province_allocation.objects.filter(province__name = province).update(maize = int(selected_province.maize) - int(maize))
            province_allocation.objects.filter(province__name = province).update(fertilizer = int(selected_province.fertilizer - int(fertilizer)))
            province_allocation.objects.filter(province__name = province).update(sorghum = int(selected_province.sorghum - int(sorghum)))

            Newfarms.objects.filter(gid = farm).update(status = "Allocated")

            return redirect("/")



    for provinces in provinces_allocated:
        maize_total += provinces.maize
        sorghum_total += provinces.sorghum
        fertilizer_total += provinces.fertilizer



    context = {
        'allocated_count':allocated_count,
        'not_allocated_count':not_allocated_count,
        'maize_total':maize_total,
        'sorghum_total':sorghum_total,
        'fertilizer_total':fertilizer_total,
        'allocationForm':allocationForm,
        'provinces_allocated':provinces_allocated,
    }
    return render(request, 'index.html', context)


def FarmSearch(request):
    query = Q()
    
    if 'status' in request.GET:
        status = request.GET['status']
        print(status)

    if 'name' in request.GET:
        name = request.GET['name']
        print(name)
    
    if 'province' in request.GET:
        province = request.GET['province']
        print(province)
    
    if 'district' in request.GET:
        district = request.GET['district']
        print(district)


        query = query.add(Q(status = status) & Q(province=province) | Q(district=district), Q.AND)
        
      
    data = Newfarms.objects.filter(query).all()
    geojson = serialize('geojson', data)
    return data.count(),  geojson, data


def MapSearch(request, search_option=''):
    count = None
    response = None
    if search_option == 'fm-street-address':
        count, geojson_data, property_list = FarmSearch(request)

    geometry = json.dumps(json.loads(geojson_data))

    if count == 0:
        pass
        
    if count == 1:
        response = {'count': count, 'geojson_data': geometry, 'property_list': property_list[0] }
        return render(request, 'home/property.html', response )
    
    else:
        response = {'count': count, 'geojson_data': geometry, 'property_list': property_list }
        return render(request, 'home/properties.html', response )
    
