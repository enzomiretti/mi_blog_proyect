from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm  # Asegúrate de que este import esté presente
from .models import Blog  # Asegúrate de importar el modelo Blog

# Vista para la página de inicio
def home(request):
    return render(request, 'home.html')  # Asegúrate de crear un archivo home.html en tu carpeta de plantillas.

# Vista para crear un nuevo blog
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)  # Incluir FILES para manejar imágenes
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirigir a la vista home después de crear el blog
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})

# Vista para listar todos los blogs
def blog_list(request):
    blogs = Blog.objects.all()  # Obtiene todos los blogs de la base de datos
    return render(request, 'blog_list.html', {'blogs': blogs})  # Renderiza la plantilla con la lista de blogs

# Vista para ver los detalles de un blog
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)  # Obtiene el blog por la clave primaria
    return render(request, 'blog_detail.html', {'blog': blog})
