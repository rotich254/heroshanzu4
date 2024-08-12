from django.shortcuts import render
from firebase_admin import storage
from datetime import timedelta
from gallery.models import Image
from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from .models import ContactSubmission, Subscriber, Admission
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
    if request.method == 'POST':
        nemis=request.POST.get('nemis')
        name=request.POST.get('name')
        middle_name = request.POST.get('middle_name')
        surname = request.POST.get('surname')
        date_of_birth = request.POST.get('date_of_birth')
        gender=request.POST.get('gender')
        grade_level=request.POST.get('grade_level')
        current_school=request.POST.get('current_school')
        about_us=request.POST.get('about_us')
        parent_name=request.POST.get('parent_name')
        parent_email=request.POST.get('parent_email')
        parent_phone=request.POST.get('parent_phone')
        parent_relation=request.POST.get('parent_relation')
        parent_residence=request.POST.get('parent_residence')
        
        Admission.objects.create(
            nemis=nemis,
            name=name,
            middle_name=middle_name,
            surname=surname,
            date_of_birth=date_of_birth,
            gender=gender,
            grade_level=grade_level,
            current_school=current_school,
            about_us=about_us,
            parent_name=parent_name,
            parent_email=parent_email,
            parent_phone=parent_phone,
            parent_relation=parent_relation,
            parent_residence=parent_residence
        )
        
        subject= f'Application for Heros Academy Admission' 
        body = (
            f'Dear {parent_name},\n\n'
            f'We have received your application for the student, {name} {middle_name} {surname}.\n\n'
            f'Below are the details provided in the application:\n'
            f'- Student Name: {name} {middle_name} {surname}\n'
            f'- Nemis: {nemis}\n'
            f'- Date of Birth: {date_of_birth}\n'
            f'- Gender: {gender}\n'
            f'- Grade Level: {grade_level}\n'
            f'- Current School: {current_school}\n\n'
            f'Thank you for your application. We will review the details and get back to you soon.\n\n'
            f'Best regards,\n'
            f'Heros Shanzu Academy'
        )
        
        emailmessage= EmailMessage(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [parent_email],            
        )       
        
        try:
            emailmessage.send()
            messages.success(request, 'Your Application Has Been Successful. We will contact you after review. Thank You')    
        except Exception as e:
            messages.error(request, f'Application error : {e}')
            
        return redirect(reverse('make_application'))
       
    else:
        return render(request, 'gallery/apply.html')