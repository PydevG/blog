from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
from django.utils import timezone

current_time = timezone.now()


User = get_user_model()



DESIGNATION_CHOICES = [
    ('chaiperson','chairperson'),
    ('secretary','secretary'),
    ('finance manager','finance manager'),
    ('Product manager','Product manager'),
]

# Create your models here.
    
class Department(models.Model):
    name = models.CharField(max_length=40)
    manager = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    department =  models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.first_name
  
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    posttype = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media', blank=False, null=False)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
class Staff(models.Model):
    details = models.ForeignKey(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100, choices=DESIGNATION_CHOICES)
    profilepic = models.ImageField(upload_to='media', blank=False)
    
    def __str__(self):
        return self.details.username
    
class Message(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.subject