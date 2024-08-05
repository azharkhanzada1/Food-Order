from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your views here.
@login_required(login_url="/login/")
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        # recipes_image = request.FILES['recipe_image']

        # print(f"this recipe name is {recipes_name} and recipest description is {recipes_description}, image is {recipes_image}")
        Recipes.objects.create(
            recipe_name =  recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image,
            )
        return redirect('/')
    
    queryset = Recipes.objects.all()
    if request.GET.get("search"):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
    context = {'recipes': queryset}

    return render(request, 'recipes.html', context)

@login_required(login_url="/login/")
def update_recipe(request, id):
    queryset = Recipes.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/')
    context = {'recipe': queryset}
    return render(request, 'update_recipes.html', context)


@login_required(login_url="/login/")
def delete_recipe(request, id): 
    queryset = Recipes.objects.get(id = id)
    queryset.delete()
    return redirect('/')


def login_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username")
            return redirect('/login/')

        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect('/')    
    return render(request, "login.html")

def logout_page(request):
    logout(request)
    return redirect("/login/")


def register_page(request):
    # breakpoint()
    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username Already Taken")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
           )
        user.set_password(password)
        user.save()
        messages.info(request, "Accoutn Created Successfully")
        return redirect("/login/")

    return render(request, 'register.html')