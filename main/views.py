from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *
from .models import Media

# Create your views here.

def homePage(request):
    user = request.user
    context = {'user': user}
    return render(request, "main/home.html", context)


def loginPage(request):
    user = request.user
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

    context = {'form': form, 'user': user}
    return render(request, 'main/login.html', context)


def signupPage(request):
    form = SignupForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    context = {'form': form}
    return render(request, "main/signup.html", context)


def infoPage(request):
    user = request.user
    context = {'user': user}
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
            user = form.save(commit=False)  # Don't save the User instance yet

            # Save the uploaded image in Media model
            if 'avatar' in request.FILES:  # Check if avatar is being updated
                avatar = Media(file=request.FILES['avatar'])
                avatar.save()

                # Associate the User instance with the Media instance
                user.avatar = avatar

            # Save user after the updates
            user.save()
            return redirect('profile')
        else:
            # If the form is not valid, print out the form errors
            print(form.errors)
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'main/editprofile.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('home')