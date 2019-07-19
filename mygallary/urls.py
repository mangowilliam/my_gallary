from django.conf.urls import url
from . import views



urlpatterns = [
    url('^$', views.gallary,name = 'gallary'),
]