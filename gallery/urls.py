from django.urls import path
from .views import index, image_gallery,make_application

urlpatterns = [
    path('', index, name='index'),
    path('gallery/', image_gallery, name='gallery'),
    path('make-application/', make_application, name='make_application')   
]
