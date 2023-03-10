from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.

class CustomUser(AbstractUser):
    is_landlord = models.BooleanField(default=False)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    gender = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100)
    school = models.CharField(max_length=100, null=True, blank=True)
    level = models.CharField(max_length=100, null=True, blank=True)

    # LANDLORDS DETAILS
    location = models.CharField(max_length=100, null=True, blank=True)
    
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    gender = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=100)
    school = models.CharField(max_length=100, null=True, blank=True)
    level = models.CharField(max_length=100, null=True, blank=True)

    # LANDLORDS DETAILS
    location = models.CharField(max_length=100, null=True, blank=True)
    


    def save(self, *args, **kwargs):
        self.id = self.user.id
        self.username = self.user.username
        self.firstName = self.user.firstName
        self.lastName = self.user.lastName
        self.gender = self.user.gender
        self.email = self.user.email
        self.phone_number = self.user.phone_number
        self.school = self.user.school
        self.level = self.user.level

        #LANDLORDS DETAILS
        self.location = self.user.location
        

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} Profile'



    

