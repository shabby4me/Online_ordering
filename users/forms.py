from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def clean_email(self):
        email1 = self.cleaned_data.get('email')
        if (email1 and  User.objects.filter(email=email1).exists()):
            raise forms.ValidationError('This email address has already registered.')
        return email1