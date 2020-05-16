from django.urls import path
from . import views

app_name = 'calleasy_firstapp'

urlpatterns = [
path('electrician/',views.electrician,name='electrician'),
path('',views.index, name='index'),
path('services/',views.services,name='services'),
path('privacy_policy/',views.privacy_policy,name='privacy_policy'),
path('about_us/',views.about_us,name='about_us'),
path('contact_us/',views.contact_us,name='contact_us'),
path('register/',views.websiteusers,name='websiteusers'),
path('signup/',views.register,name='register'),
path('user_login/',views.user_login,name='user_login'),

]
