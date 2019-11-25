from django.shortcuts import render
from django.contrib.auth import logout
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse


def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
