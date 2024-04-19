from rest_framework import serializers
from .models import Category,City, Tour

class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    imageLink = serializers.CharField(max_length=255)


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