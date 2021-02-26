from django.db import models
from django.contrib.auth.models import User


class userInfo(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    phone = models.IntegerField()
    profile_pic = models.ImageField(
        upload_to='user/', default='user/default.png', null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class jobPost(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    salaryL = models.PositiveIntegerField()
    salaryH = models.PositiveIntegerField()
    min_exp = models.CharField(max_length=20)
    description = models.TextField()
    resume = models.CharField(max_length=200)
    category = models.CharField(max_length=20, default="coding")

    def __str__(self):
        return self.company
