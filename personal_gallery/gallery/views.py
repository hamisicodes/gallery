from django.shortcuts import render
from .models import Image,Category

# Create your views here.

def image_list(request):
    images  = Image.objects.all()[:8]

    return render(request,'index.html' , {'images':images})

def category(request,name):
    category = Category.objects.get(name = name)
    images = Image.objects.filter(category = category)

    return render(request,'category.html' , {'images':images , 'category': category})
