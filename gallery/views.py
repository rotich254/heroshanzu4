from django.shortcuts import render
from firebase_admin import storage
from datetime import timedelta
from gallery.models import Image
from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from .models import ContactSubmission, Subscriber
from django.conf import settings

def index(request):
    
    if request.method == 'POST':
        if 'subscribe' in request.POST:
            email= request.POST.get('subscribe_email')
            
            subscriber, created= Subscriber.objects.get_or_create(email=email)
            
            if created:
                subject= 'Welcome To Our Newsletter'
                body = (
                    f'Dear {email},\n'
                    'Thank You for Subscribing to our Newsletter! We are excited to have you onboard with latest news.\n\n'
                    'Best Regards,\n'
                    'Heros A.I.C. Shanzu'                    
                )
                
                emailmessage = EmailMessage(
                    subject,
                    body,
                    settings.EMAIL_HOST_USER,
                    [email],
                    
                )
                
                try:
                    emailmessage.send()
                    messages.success(request, 'Subscription Successful! A confirmation Email Has Been Sent to You')
                    
                except Exception as e:
                    messages.error(request, f'Error Occured During Subscription: {e}')
                    
            return redirect(reverse('index') + '#footer' )
        
        else:
            
            name= request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            
            ContactSubmission.objects.create(name=name,email=email,message=message)
            
            subject = f'Contact Submission by {name}'
            
            emailmessage= EmailMessage(
                subject,
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                to=[settings.EMAIL_HOST_USER],
                reply_to = [email],
            )  
            
            try:
                emailmessage.send()
                messages.success(request, 'Message Has Been Sent Successfully')            
                
            except Exception as e:
                messages.error(request, f'An Error Has Occured, {e}')
          
            return redirect(reverse('index') + '#contact')
      
    else:
        return render(request, 'gallery/index.html')

# def image_gallery(request):
#     images = Image.objects.all()
#     return render(request, 'gallery/media.html', {'images': images})

def image_gallery(request):
    bucket = storage.bucket()
    blobs = bucket.list_blobs()
    images = []

    for blob in blobs:
        if blob.content_type.startswith('image/'):
            image_url = blob.generate_signed_url(timedelta(seconds=300), method='GET')
            images.append({'image_url': image_url})

    return render(request, 'gallery/media.html', {'images': images})

def make_application(request):
    return render(request, 'gallery/apply.html')