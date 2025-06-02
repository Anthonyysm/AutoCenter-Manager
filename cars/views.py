from django.shortcuts import render, HttpResponse
from cars.models import Car


def cars_view(request):
    cars = Car.objects.all().order_by('brand__name')
    search = request.GET.get('search')

    if search:
        cars = cars.filter(model__icontains=search)

    return render(request, 'cars.html', {'cars': cars})


def new_car_view(request):
    return HttpResponse('new car view')