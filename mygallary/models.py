from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        
    def save_image(self):
        self.save()

class Location(models.Model):
    locale = models.CharField(max_length = 60)
    
    def __str__(self):
        return self.locale
    
    def save_location(self):
        self.save()
    
class Category(models.Model):
    variety = models.CharField(max_length = 60)
    
    
    def __str__(self):
        return self.variety
    
    def save_category(self):
        self.save()