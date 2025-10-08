from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(

        widget=forms.EmailInput(attrs={
            'placeholder': 'twój@email.com',
            'class': 'text-center',
        }),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'hasło',
            'class': 'text-center',
        }),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'recydywa hasła',
            'class': 'text-center',
        })
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets ={
            "username": forms.TextInput(attrs={
                "placeholder": "zaskocz mnie",
                 "class": "text-center"}),

        }



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus": "on",
        "placeholder": "ta, którą zapomniałeś",
        "class": "text-center font-semibold"
    })
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            "placeholder": "to, które miałeś pamiętać",
            "class": "text-center font-semibold"
        })

    )