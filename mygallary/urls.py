from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views



urlpatterns = [
    url('^$', views.gallary,name = 'gallary'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
    
    
    
    
    
    
    
    #self.fufu= Image(name = 'fufu',description = 'juju inside',location = self.kiambu,cetegory = self.food)
      #  def test_instance(self):
            #self.assertTrue(isinstance(self.fufu,Image))
       # def test_save(self):
        #    self.fufu.save_image()
         #   images = Image.objects.all()
          #  self.assertTrue(len(images)>0)