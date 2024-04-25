from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import City, Tour, Category
from rest_framework import status
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['GET'])
def get_all_cities(request):
    cities = City.objects.all()
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    serializer = CitySerializer(city)
    return Response(serializer.data)

@api_view(['GET'])
def tag_list(request):
    tags = Tags.objects.all()
    serializer = TagsSerializer(tags, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tag_detail(request, pk):
    tag = get_object_or_404(Tags, pk=pk)
    serializer = TagsSerializer(tag)
    return Response(serializer.data)

@api_view(['GET'])
def color_list(request):
    colors = Colors.objects.all()
    serializer = ColorsSerializer(colors, many=True)
    print(colors)
    return Response(serializer.data)

@api_view(['GET'])
def color_detail(request, pk):
    color = get_object_or_404(Colors, pk=pk)
    serializer = ColorsSerializer(color)
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

class CreateUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddToCartView(APIView):
    def post(self, request, *args, **kwargs):
        tour_id = request.data.get('tour_id')
        quantity = int(request.data.get('quantity', 1))

        try:
            tour = Tour.objects.get(id=tour_id)
        except Tour.DoesNotExist:
            return Response({'error': 'Tour not found'}, status=status.HTTP_404_NOT_FOUND)

        cart, _ = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            tour=tour,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class ClearCartView(APIView):
    def post(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        if not created:
            cart.items.all().delete()
            return Response({'message': 'Cart cleared successfully'}, status=status.HTTP_204_NO_CONTENT)
        
        return Response({'message': 'Cart was already empty'}, status=status.HTTP_204_NO_CONTENT)