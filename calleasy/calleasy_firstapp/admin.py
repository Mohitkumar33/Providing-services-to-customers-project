from django.contrib import admin
from .models import Electrician, WebsiteUser, UserProfileInfo, User
# Register your models here.
admin.site.register(Electrician)
admin.site.register(WebsiteUser)
admin.site.register(UserProfileInfo)
