# accounts/urls.py
from django.urls import path
from .views import signup, CustomLoginView, profile

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
]
