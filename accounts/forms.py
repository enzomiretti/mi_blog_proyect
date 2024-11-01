
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        error_messages = {
            'username': {
                'required': "Este campo es obligatorio.",
                'max_length': {
                    'message': "Asegúrate de que no exceda los 150 caracteres.",
                },
            },
            'email': {
                'required': "Este campo es obligatorio.",
            },
            'password': {
                'required': "Este campo es obligatorio.",
            },
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password']) 
        if commit:
            user.save()
        return user
