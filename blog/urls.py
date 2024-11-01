from django.urls import path
from .views import home, create_blog, blog_list, blog_detail, delete_blog

urlpatterns = [
    path('', home, name='home'),  
    path('create/', create_blog, name='create_blog'), 
    path('blogs/', blog_list, name='blog_list'),  
    path('blogs/<int:pk>/', blog_detail, name='blog_detail'),
    path('blogs/<int:pk>/delete/', delete_blog, name='delete_blog'), 
]
