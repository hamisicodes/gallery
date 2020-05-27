from django.test import TestCase
from .models import Image,Location,Category
from django.contrib.auth.models import User

# Create your tests here.
class categoryTest(TestCase):
    def setUp(self):
        self.new_category = Category(name='anything' ,description = 'nothing')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))

    def test_save_method(self):
        self.new_category.save_category()
        categories = Category.objects.all()

        self.assertTrue(len(categories) > 0)

    def test_delete_method(self):
        self.new_category.save_category()
        self.new_category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)



class LocationTest(TestCase):
    def setUp(self):
        self.new_location = Location(name='Madagascar')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    def test_save_method(self):
        self.new_location.save_location()
        locations = Location.objects.all()

        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.new_location.save_location()
        self.new_location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

class ImageTest(TestCase):
    def setUp(self):
        self.publisher = User.objects.create(username='John Doe')
        self.location = Location.objects.create(name = 'Madagascar')
        self.category = Category.objects.create(name = 'International' , description ='International things')
        self.new_image = Image(name='Madagascar' , description ='An Image of Madagascar',publisher = self.publisher  , location =self.location , category =self.category,)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))   


    def test_save_method(self):
        self.new_image.save_image()
        images = Image.objects.all()

        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.new_image.save_image()
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    





