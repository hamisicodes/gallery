from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    description =models.TextField(default = 'description')

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=30)
    description  = models.TextField()
    location = models.ForeignKey(Location , on_delete = models.CASCADE)
    category = models.ForeignKey(Category , on_delete =models.CASCADE)
    publisher = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='images/', default='hamisi')

    def __str__(self):
        return self.name

