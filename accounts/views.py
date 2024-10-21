# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.urls import reverse_lazy

# Vista para el registro de usuario
def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente al usuario
            return redirect('home')  # Redirige a la página de inicio después de registrarse
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})

class CustomLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    authentication_form = AuthenticationForm  # Asegúrate de que esto esté definido
    redirect_authenticated_user = True
    success_url = reverse_lazy('blog_list')


# Vista para el cierre de sesión (opcional, puedes agregarla si lo deseas)
class CustomLogoutView(auth_views.LogoutView):
    next_page = 'home'  # Redirige a la página de inicio después de cerrar sesión


def profile(request):
    return render(request, 'accounts/profile.html')