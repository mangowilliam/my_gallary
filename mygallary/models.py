from django.db import models

# Create your models here.


class Location(models.Model):
    locale = models.CharField(max_length = 60)
    
    def __str__(self):
        return self.locale
    class Meta:
            ordering = ['locale']
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
        
class Category(models.Model):
    variety = models.CharField(max_length = 60)
    
    
    def __str__(self):
        return self.variety
    class Meta:
            ordering = ['variety']
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
        
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
        
    def delete_image(self):
            self.delete()
    @classmethod     
    def get_images(cls):
        mygallary = cls.objects.all()
        return mygallary
    
    @classmethod
    def search_by_category(cls,search_term):
        mygallary = cls.objects.filter(category__icontains=search_term)
        return mygallary
        