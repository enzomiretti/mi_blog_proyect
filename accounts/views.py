
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')  
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})

class CustomLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    authentication_form = AuthenticationForm  
    redirect_authenticated_user = True
    success_url = reverse_lazy('blog_list')



from django.contrib import messages

class CustomLogoutView(auth_views.LogoutView):
    next_page = 'home'  

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Cerraste sesión") 
        return super().dispatch(request, *args, **kwargs)



def profile(request):
    return render(request, 'accounts/profile.html')