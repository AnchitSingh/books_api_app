from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='API Home'),
    path('api/external-books', views.general_data,name='External Books'),
    path('api/v1/books', views.book_api,name='Books API'),
    path('api/v1/books/<int:id>', views.book_api_patch,name='Books API'),
    
]