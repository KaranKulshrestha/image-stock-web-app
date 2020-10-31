from django.shortcuts import render
from django.http import HttpResponse
from aperastock_app.models import Category, Image

# Create your views here.

def home(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    dict = {
        'images':images,
        'categories':categories,
    }
    return render(request, "home.html", dict)

def show_about_page(request):
    name = "Aperastock"
    link = "https://www.youtube.com/"

    data = {
        'name':name,
        'link':link,
    }
    return render(request, "about.html", data) 


def show_category_page(request, cid):
    categories = Category.objects.all()

    category = Category.objects.get(pk=cid)

    images = Image.objects.filter(cat=category)


    dict = {
        'images':images,
        'categories':categories,
    }
    return render(request, "home.html", dict)