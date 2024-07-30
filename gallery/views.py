from django.shortcuts import render
from firebase_admin import storage
from datetime import timedelta
from gallery.models import Image
from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import redirect

def index(request):
    
    if request.method == 'POST':
        name= request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        subject = f'Contact Submission by {name}'
        
        emailmessage= EmailMessage(
            subject,
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            email,
            ['heroshanzu@gmail.com'],
            reply_to = [email],
        )  
        
        emailmessage.send()
        messages.success(request, 'Email Has Been Sent')
        return redirect('index')
    
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