from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Electrician(models.Model):
    name = models.CharField(max_length=256)
    jobs_done = models.PositiveIntegerField()
    skill_age = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()
    phone_number_1 = models.PositiveIntegerField()
    phone_number_2 = models.PositiveIntegerField()

class WebsiteUser(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,unique=True)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    email = models.EmailField(max_length=254,unique=True)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='calleasy_firstapp/profile_pics',blank=True)

    def __str__(self):
        return self.user.username
