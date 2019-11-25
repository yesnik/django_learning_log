from django.shortcuts import render
from django.contrib.auth import logout
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            print('=====VALID')
            new_user = form.save()
            # Log the user in and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            
            login(request, authenticated_user)
            
            return HttpResponseRedirect(reverse('learning_logs:index'))
        else:
            print('===== NOT  VALID')
    context = {'form': form}
    return render(request, 'users/register.html', context)