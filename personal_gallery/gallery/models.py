from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
         self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        pass

class Category(models.Model):
    name = models.CharField(max_length=30)
    description =models.TextField(default = 'description')

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        pass
    



class Image(models.Model):
    name = models.CharField(max_length=30)
    description  = models.TextField()
    location = models.ForeignKey(Location , on_delete = models.CASCADE)
    category = models.ForeignKey(Category , on_delete =models.CASCADE)
    publisher = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='images/', default='hamisi')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-category']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        pass

    @classmethod
    def get_image_by_id(cls ,id):
        image = cls.objects.get(id = id)
        return image

    @classmethod
    def search_image(cls,category):
        categ = Category.filter(name = category)
        images = cls.objects.filter(category = categ)
        return images

    @classmethod
    def filter_by_location(cls,location):
        images = cls.objects.filter(location = location)


    



        

