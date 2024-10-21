from django.urls import path
from .views import home, create_blog, blog_list, blog_detail

urlpatterns = [
    path('', home, name='home'),  # Página de inicio
    path('create/', create_blog, name='create_blog'),  # Crear un nuevo blog
    path('blogs/', blog_list, name='blog_list'),  # Listar todos los blogs
    path('blogs/<int:pk>/', blog_detail, name='blog_detail'),  # Detalle de un blog
]
