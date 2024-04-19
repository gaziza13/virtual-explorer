from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
# router.register(r'cities', CityViewSet)
# router.register(r'tours', TourViewSet)


urlpatterns = [
    path('categories/', get_categories, name='get_categories'),
    path('categories/<int:category_id>/cities/', get_cities_by_category, name='get_cities_by_category'),
    path('tours/', get_tours, name='get_tours'),
    path('tours/<int:tour_id>/', get_tour_detail, name='get_tour_detail'),
    path('cities/', get_all_cities, name='get_all_cities'),
    path('cities/<int:id>/', get_city, name='get_city'),
    path('cities/<int:city_id>/tours/', get_city_tours, name='get_city_tours'),

    
]