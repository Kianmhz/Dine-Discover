from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.homePage, name='home'),
    path("login/", views.loginPage, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    path("signup/", views.signupPage, name='signup'),
    path("info/", views.infoPage, name='info'),
    path("aboutus/", views.aboutUsPage, name='about'),
    path("contact/", views.contactPage, name='contact'),
    path("userprofile/", views.userprofilePage, name='profile'),
    path("reviews/", views.reviewsPage, name='reviews'),
    path("editprofile/", views.editprofilePage, name='editP'),
    path('reset_password/', auth_views.PasswordResetView.as_view(
            template_name="main/registration/password_reset_form.html",
            email_template_name="main/registration/password_reset_email.html",
            subject_template_name="main/registration/password_reset_subject.txt"), 
        name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
            template_name="main/registration/password_reset_done.html"), 
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name="main/registration/password_reset_confirm.html"), 
        name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
            template_name="main/registration/password_reset_complete.html"), 
        name='password_reset_complete'),
]
