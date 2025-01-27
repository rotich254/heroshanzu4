from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class ContactSubmission(models.Model):
    name= models.CharField(max_length=40)
    email= models.EmailField()
    message= models.TextField(max_length=200)
    submitted_at= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name} - {self.email}'

class Subscriber(models.Model):
    email= models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email

class Admission(models.Model):
    GRADE_LEVEL_CHOICES = [
        ('pp1', 'Pre Primary 1'),
        ('pp2', 'Pre Primary 2'),
        ('grade1', 'Grade 1'),
        ('grade2', 'Grade 2'),
        ('grade3', 'Grade 3'),
        ('grade4', 'Grade 4'),
        ('grade5', 'Grade 5'),
        ('grade6', 'Grade 6'),
        ('grade7', 'Grade 7'),
        ('grade8', 'Grade 8'),
        ('grade9', 'Grade 9') 
    ]
    RELATION_CHOICES = [
        ('parent', 'Parent'),
        ('guardian', 'Guardian'),
        ('other','Other')
    ]
    GENDER_CHOICES = [
        ('male','Male'),
        ('female', 'Female')
    ]
    learner_upi= models.CharField(max_length=50)
    name= models.CharField(max_length=40)
    middle_name= models.CharField(max_length=40)
    surname= models.CharField(max_length=40)
    date_of_birth= models.DateField()
    gender= models.CharField(choices=GENDER_CHOICES, max_length=10)
    grade_level= models.CharField(choices=GRADE_LEVEL_CHOICES, max_length=40)
    current_school= models.CharField(max_length=200, blank=True)
    about_us= models.TextField(max_length=200)
    parent_name= models.CharField(max_length=100)
    parent_email= models.EmailField()
    parent_phone = models.CharField(max_length=15)
    parent_relation= models.CharField(choices=RELATION_CHOICES, max_length=20)
    parent_residence= models.CharField(max_length=40)
    
    def __str__(self):
        return f'{self.name} {self.middle_name} {self.surname}'