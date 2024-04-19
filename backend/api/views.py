from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import City, Tour, Category
from rest_framework import status
from .serializers import CitySerializer, TourSerializer, CategorySerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def get_all_cities(request):
    cities = City.objects.all()
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_cities_by_category(request, category_id):
    tours = Tour.objects.filter(categories__id=category_id)
    
    city_ids = tours.values_list('city', flat=True).distinct()
    
    cities = City.objects.filter(id__in=city_ids)
    serializer = CitySerializer(cities, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_city(request, id):
    city = get_object_or_404(City, id=id)
    serializer = CitySerializer(city)
    return Response(serializer.data)

@api_view(['GET'])
def get_city_tours(request, city_id):
    tours = Tour.objects.filter(city_id=city_id)
    serializer = TourSerializer(tours, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    serializer = TourSerializer(tour)
    return Response(serializer.data)

@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_tours(request):
    tours = Tour.objects.all()
    serializer = TourSerializer(tours, many=True)
    return Response(serializer.data)


