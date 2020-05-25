from  django.urls import path
from  . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('' , views.image_list , name = 'image_list'),
    path('category/<name>' , views.category , name = 'category')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)