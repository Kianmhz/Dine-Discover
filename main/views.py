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
    context = {}
    return render(request, "main/userprofile.html", context)


def reviewsPage(request):
    context = {}
    return render(request, "main/reviews.html", context)


def editprofilePage(request):
    context = {}
    return render(request, "main/editprofile.html", context)


def addrestaurantPage(request):
    context = {}
    return render(request, "main/addR.html", context)