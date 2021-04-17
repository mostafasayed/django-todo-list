from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


def logout_view(request):
    logout(request)
    return redirect('/login')
