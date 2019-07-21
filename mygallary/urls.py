from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views



urlpatterns = [
    url('^$', views.gallary,name = 'gallary'),
    url(r'^search/', views.search_image, name='search_image'),
    url(r'^details/(\d+)',views.get_image_by_id,name ='details')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
    
    
    
    
    
    
    
    