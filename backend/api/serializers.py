from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    imageLink = serializers.CharField(max_length=255)
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
    
    class Meta:
        model = City
        fields = ['id', 'name', 'description', 'imageLink', 'tags']

    def to_representation(self, instance):
        representation = super(CitySerializer, self).to_representation(instance)
        representation['tags'] = [tag.name for tag in instance.tags.all()]
        return representation


    def create(self, validated_data):
        instance = City.objects.create(
            name=validated_data.get('name'),
            description=validated_data.get('description'),
            imageLink=validated_data.get('imageLink')
        )

        return instance
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.imageLink = validated_data.get('imageLink', instance.imageLink)

        instance.save()

        return instance

    def delete(self, instance):
        instance.delete()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

class CityTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ('id', 'name', 'description', 'price', 'duration')


class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ['id', 'name', 'hex_value']

class TagsSerializer(serializers.ModelSerializer):
    color = serializers.SlugRelatedField(
        queryset=Colors.objects.all(),
        slug_field='hex_value'
    )
    
    class Meta:
        model = Tags
        fields = ['id', 'name', 'color']

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'tour', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'items']