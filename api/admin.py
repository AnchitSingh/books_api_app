from django.contrib import admin
from django.urls import path,include
from .models import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]

admin.site.register(items)
admin.site.register(author)