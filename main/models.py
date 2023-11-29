from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Media(models.Model):
    file = models.ImageField(upload_to='media/')


class User(AbstractUser):
    email = models.EmailField("Email", max_length=150, unique=True)
    username = models.CharField("Username", max_length=20, unique=True)
    about = models.TextField(null=True, blank=True)
    avatar = models.ForeignKey(Media, on_delete=models.DO_NOTHING, null=True, blank=True)
    date_joined = models.DateField("Date Joined", auto_now_add=True)


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)


class Review(models.Model):
    RATING_CHOICES = [
        (1.0, '★☆☆☆☆'),
        (2.0, '★★☆☆☆'),
        (3.0, '★★★☆☆'),
        (4.0, '★★★★☆'),
        (5.0, '★★★★★'),
    ]

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.FloatField(choices=RATING_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)