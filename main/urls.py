from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.homePage, name='home'),
    path("login/", views.loginPage, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    path("signup/", views.signupPage, name='signup'),
    path("resetpass/", views.resetPassPage, name='passR'),
    path("info/", views.infoPage, name='info'),
    path("aboutus/", views.aboutUsPage, name='about'),
    path("contact/", views.contactPage, name='contact'),
    path("userprofile/", views.userprofilePage, name='profile'),
    path("reviews/", views.reviewsPage, name='reviews'),
    path("editprofile/", views.editprofilePage, name='editP'),
    path("addrestaurant/", views.addrestaurantPage, name='addR'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
