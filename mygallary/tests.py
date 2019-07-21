from django.test import TestCase
from .models import Location, Category, Image


# Create your tests here.
class LocationTestclass(TestCase):
    def setUp(self):
        self.kiambu = Location(locale = 'kiambu')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.kiambu,Location))
        
    def test_save(self):
        self.kiambu.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

class CategoryTestclass(TestCase):
    def setUp(self):
        self.food = Category(variety = 'food')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))
    
    def test_save(self):
        self.food.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)