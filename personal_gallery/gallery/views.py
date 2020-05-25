from django.shortcuts import render
from .models import Image,Category,Location

# Create your views here.

def image_list(request):
    images  = Image.objects.all()[:8]

    return render(request,'index.html' , {'images':images})

def category(request,name):

    category = Category.objects.get(name = name)
    images = Image.objects.filter(category = category)


    return render(request,'category.html' , {'images':images , 'category': category })

def location(request,name):

    location = Location.objects.get(name = name)
    images = Image.objects.filter(location = location)


    return render(request,'location.html' , {'images':images , 'location': name })


def search_results(request):

    if 'result' in request.GET and request.GET["result"]:
        search_term = request.GET.get("result")
        searched_images = Image.searchimage(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
