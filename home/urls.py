from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('send_email/', views.send_email, name="send_email"),
]