from django.contrib import admin
from django.urls import path, include
from vege import views

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('delete_recipe/<id>/', views.delete_recipe, name='delete_recipe'),
    path('update_recipe/<id>/', views.update_recipe, name='update_recipe'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('logout/', views.logout_page, name="logout_page"),
    
]
