from django.shortcuts import render, redirect
from .utils import send_email_email
from django.http import HttpResponse

# Create your views here.
def send_email(request):
    send_email_email()
    return redirect('/contact/')  # Redirect to contact page after sending email

def index(request):
    peoples = [
        {'name' : "azhar khan", 'age' : 20},
        {'name' : "zubari khan", 'age' : 19},
        {'name' : "jedi khan", 'age' : 21},
        {'name' : "ali khan", 'age' : 26},
    ]
    veg = ["Pumpkin", "Tomato", "Patato"]
    return render (request, 'index.html', context={'peoples': peoples, "veg": veg})



def contact(request):
    return render (request, "contact.html")


def about(request):
    return render (request, "about.html")