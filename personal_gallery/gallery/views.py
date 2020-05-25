from django.shortcuts import render
from .models import Image

# Create your views here.

def image_list(request):
    images  = Image.objects.all()[:8]

    return render(request,'index.html' , {'images':images})
