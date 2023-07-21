from django.urls import path
from .import views


urlpatterns = [
path('signup/',views.register,name='signup'),
path('login/',views.user_login,name='login'),
path('appointment/',views.appoinment,name='appointment'),
path('service/',views.service,name='service'),
path('service_1/',views.service_1,name='service_1'),
path('service_2/',views.service_2,name='service_2'),
path('service_3/',views.service_3,name='service_3'),
path('service_4/',views.service_4,name='service_4'),


path('',views.home,name='home'),
path('about/',views.about,name='about'),
path('gallery/',views.gallery,name='gallery'),
path('team/',views.team,name='team'), 
path('blog/',views.blog,name='blog'),
path('contact/',views.contact,name='contact'),

path('log/',views.log,name='log'),
path('verify_otp/',views.verify_otp,name='verify_otp'),
] 