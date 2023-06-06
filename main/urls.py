from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name='home'),
    path("login/", views.loginPage, name='login'),
    path("signup/", views.signupPage, name='signup'),
    path("info/", views.infoPage, name='info'),
    path("aboutus/", views.aboutUsPage, name='about'),
    path("contact/", views.contactPage, name='contact'),
    path("userprofile/", views.userprofilePage, name='profile'),
    path("reviews/", views.reviewsPage, name='reviews'),
    path("editprofile/", views.editprofilePage, name='editP'),
]
