from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def homePage(request):
    user = request.user
    context = {'user': user}
    return render(request, "main/home.html", context)


def loginPage(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()

    user = request.user
    context = {'form': form, 'user': user}
    return render(request, 'main/login.html', context)


def signupPage(request):
    context = {}
    return render(request, "main/signup.html", context)


def resetPassPage(request):
    context = {}
    return render(request, "main/passReset.html", context)


def infoPage(request):
    context = {}
    return render(request, "main/info.html", context)


def aboutUsPage(request):
    context = {}
    return render(request, "main/aboutus.html", context)


def contactPage(request):
    context = {}
    return render(request, "main/contact.html", context)


def userprofilePage(request):
    user = request.user
    context = {'user': user}
    return render(request, "main/userprofile.html", context)


def reviewsPage(request):
    context = {}
    return render(request, "main/reviews.html", context)


def editprofilePage(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'main/editprofile.html', {'form': form})


def addrestaurantPage(request):
    context = {}
    return render(request, "main/addR.html", context)


def logoutUser(request):
    logout(request)
    return redirect('home')