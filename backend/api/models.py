from django.db import models
from django.conf import settings
# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=100, unique=True)
    color = models.ForeignKey('Colors', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Colors(models.Model):
    name = models.CharField(max_length=100, unique=True)
    hex_value = models.CharField(max_length=7)

    def __str__(self):
        return self.name
    

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    imageLink = models.TextField()
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        tags = ", ".join(tag.name for tag in self.tags.all())
        return f"{self.name} (ID: {self.id}) {self.tags} dd"

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
    

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    

