from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('gallery/', image_gallery, name='gallery'),
    path('our-school/', school, name='school'),
    path('staff/', staff, name='staff'),
    path('make-application/', make_application, name='make_application'),
    path('checkout/',donation_checkout, name='checkout'),
    path('mpesa-payment/', mpesa_payment, name='mpesa_payment'),
    path('callback/', mpesa_callback, name='mpesa_callback'),
]
