from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

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

    path('tags/', tag_list, name='tag-list'),
    path('tags/<int:pk>/', tag_detail, name='tag-detail'),
    path('colors/', color_list, name='color-list'),
    path('colors/<int:pk>/', color_detail, name='color-detail'),

    path('auth/register/', CreateUserView.as_view(), name='create_user'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('clear-cart/', ClearCartView.as_view(), name='clear-cart'),
    
]