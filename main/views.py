from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *
from .models import Media
import os
import requests
import uuid
import dotenv

dotenv.load_dotenv()

# Create your views here.

def getRestaurantLogo(query):
    query = query.replace(" ", "%20")

    endpoint = "https://api.brandfetch.io/v2/search/" + query
    headers = {
        "Authorization": os.getenv("logoAPI"),
    }

    response = requests.get(endpoint, headers=headers)
    data = response.json()
    fileted_data = []

    fields_to_include = ['name', 'icon', 'logo']
    for suggestion in data:
        filtered_suggestion = {key: suggestion.get(key) for key in fields_to_include if suggestion.get(key) != None}
        if filtered_suggestion.get("icon") or filtered_suggestion.get("logo"):
            fileted_data.append(filtered_suggestion)

    return fileted_data[0].get("logo") if fileted_data[0].get("logo") else fileted_data[0].get("icon")

    

def findRestaurants(query, limit):
    endpoint = "https://api.mapbox.com/search/searchbox/v1/suggest"
    access_token = os.getenv("locationAPI")
    session_token = uuid.uuid4()

    params = {
        "access_token": access_token,
        "session_token": session_token,
        "q": query,
        "limit": 10
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    restaurant_suggestions = [suggestion for suggestion in data["suggestions"] if suggestion.get('maki') == 'restaurant' and suggestion.get('context', {}).get('country', {}).get('name') == 'Canada']
    restaurant_suggestions = restaurant_suggestions[:limit]
    filtered_restaurant_suggestions = []

    fields_to_include = ['name', 'address', 'full_address', 'place_formatted']
    for suggestion in restaurant_suggestions:
        filtered_suggestion = {key: suggestion[key] for key in fields_to_include}
        filtered_suggestion["image"] = getRestaurantLogo(filtered_suggestion.get("name"))
        filtered_restaurant_suggestions.append(filtered_suggestion)

    return filtered_restaurant_suggestions

def homePage(request):
    user = request.user

    q = request.GET.get('q') if (request.GET.get('q') != None) else 'tim'
    restaurants = findRestaurants(query=q, limit=6)

    context = {'user': user, "restaurants": restaurants}
    return render(request, "main/home.html", context)


def loginRegisterPage(request):
    user = request.user
    login_form = LoginForm()
    register_form = form = SignupForm()
    context = {'login_form': login_form,
               'register_form': register_form, 'user': user}
    return render(request, 'main/login_register.html', context)


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
    return redirect('login_register')

def signupPage(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return redirect('login_register')
    else:
        return redirect('home')


def infoPage(request):
    user = request.user
    form = ReviewForm(request.POST or None)
    context = {'user': user, 'form': form}
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
        form = UserUpdateForm(request.POST, request.FILES,
                              instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save the User instance yet

            # Save the uploaded image in Media model
            if 'avatar' in request.FILES:  # Check if avatar is being updated
                file = request.FILES['avatar']
                file.name = f"{user.username}.png"
                try:
                    os.remove(f"./media/media/{user.username}.png")

                except:
                    pass
                avatar = Media(file=file)
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