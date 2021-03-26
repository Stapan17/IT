from django.contrib import admin
from .models import User, userInfo, jobPost, Category, contactUS


admin.site.register(userInfo)
admin.site.register(jobPost)
admin.site.register(Category)
admin.site.register(contactUS)
