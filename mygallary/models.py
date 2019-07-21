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
        
    def update_location(self):
        self.delete()
    
    def delete_category(self):
        self.update()
        
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
        
    def update_category(self):
        self.update()
        
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    
    def __str__(self):
        return self.category
        
    def save_image(self):
        self.save()
        
    @classmethod 
    def delete_image(id):
        self.delete()
        
    @classmethod     
    def get_images(cls):
        mygallary = cls.objects.all()
        return mygallary
    
    @classmethod
    def search_image(cls,items):
        mygallary = cls.objects.filter(categories__variety__icontains=items)
        return mygallary
    @classmethod
    def get_image_by_id(cls,id):
        mygallary=Image.objects.get(id=id)
        return mygallary
    
    def update_image_by_id(id):
        mygallary = cls.objects.update(id=id)
        return mygallary
    