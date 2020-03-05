from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import forms
from django.contrib.auth import authenticate, login


# Create your views here.
def login(request):

    return render(request,'book/signup.html')

def signup(requests):
    h = UserCreationForm(requests.POST or None)
    if h.is_valid():
        h.save()
        username = h.cleaned_data.get('username')
        raw_password = h.cleaned_data.get('password')
        user = authenticate(username=username, password=raw_password)
        login(requests,user)
        return redirect('branch')
    return render(requests, 'book/signup.html', {'form': h})


def login(request):
    g = AuthenticationForm(request.POST)
    if g.is_valid():
        # logging in
        user = form.get_user()
        login(request,user)
        return redirect('branch')
    return render(request, 'book/login.html',{'form':g})
