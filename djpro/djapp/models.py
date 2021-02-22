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
