from django.test import TestCase

from .models import Category, Image, Location


# Create your tests here.
class LocationTestclass(TestCase):
    def setUp(self):
        self.kiambu = Location(locale='kiambu')

    def test_instance(self):
        self.assertTrue(isinstance(self.kiambu, Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save(self):
        self.kiambu.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete(self):
        self.kiambu.save()
        self.kiambu.delete()
        self.assertTrue(len(Location.objects.all()) == 0)

    def test_update(self):
        self.kiambu.save()
        self.kiambu.variety = 'kajiado'
        self.assertTrue(self.kiambu.locale == 'kajiado')


class CategoryTestclass(TestCase):
    def setUp(self):
        self.food = Category(variety='food')

    def test_instance(self):
        self.assertTrue(isinstance(self.food, Category))

    def tearDown(self):
        Category.objects.all().delete()

    def test_save(self):
        self.food.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete(self):
        self.food.save()
        self.food.delete()
        self.assertTrue(len(Category.objects.all()) == 0)

    def test_update(self):
        self.food.save()
        self.food.variety = 'fun'
        self.assertTrue(self.food.variety == 'fun')


class ImageTestclass(TestCase):
    def setUp(self):
        self.kiambu = Location(locale='kiambu')
        self.kiambu.save_location()

        self.food = Category(variety='food')
        self.food.save_category()

        self.new_image = Image(
        name='machakura', description='kiabuu special', location=self.kiambu, cetegory=self.food)
        self.new_image.save()

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    def test_instance(self):
        self.food.save()
        self.assertTrue(isinstance(self.food, Image))

    def test_delete(self):
        self.food.save()
        self.food.delete()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_update(self):
        self.food.save()
        self.food.variety = 'fun'
        self.assertTrue(self.food.variety == 'fun')

    def test_search_image(self):
        self.food.save()
        images = Image.search_image(self.food)
        self.assertTrue(len(images) > 0)
