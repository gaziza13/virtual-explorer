from django.db import models

# Create your models here.
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    imageLink = models.TextField()

    def __str__(self):
        return f"{self.name} (ID: {self.id})"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Tour(models.Model):
    city = models.ForeignKey(City, related_name='tours', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.DurationField()
    categories = models.ManyToManyField(Category, related_name='tours')
    imageLink = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} (ID: {self.id})"

