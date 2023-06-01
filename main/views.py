from django.shortcuts import render

# Create your views here.


def homePage(request):
    context = {}
    return render(request, "main/home.html", context)


def loginPage(request):
    context = {}
    return render(request, "main/login.html", context)


def signupPage(request):
    context = {}
    return render(request, "main/signup.html", context)


def infoPage(request):
    context = {}
    return render(request, "main/info.html", context)
