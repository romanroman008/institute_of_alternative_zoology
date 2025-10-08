from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, redirect

from users.forms import RegisterForm
from users.models import Profile


# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            username = form.cleaned_data.get('username')

            messages.success(request, f"Siemano kolano {username} :)")
            return redirect('users:login')


    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})



def logout_view(request):
    logout(request)
    messages.success(request, "Zostałeś wylogowany")
    return redirect('myapp:index')

@login_required
def profile(request):
    return render(request, 'users/profile.html')

