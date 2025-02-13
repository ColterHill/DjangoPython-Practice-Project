from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from .models import Profile
from django.views.generic.list import ListView
from django.contrib.auth import logout, login




def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, you have successfully signed up!')
            return redirect('login')
        else:
            messages.error(request, "user could not be created! Try Again!")
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})

def logout_view(request):
    logout(request)
  
    return render(request, 'users/logout.html')

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')

class UserAdminClassView(ListView):
    model = Profile;
    template_name = 'users/user-admin.html'
    context_object_name = 'user_list'

