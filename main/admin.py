from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

class UserAdminPanel(admin.ModelAdmin):
    readonly_fields = ["date_joined"]

class FoodMenuPanel(admin.ModelAdmin):
    pass

class MediaPanel(admin.ModelAdmin):
    pass

class ReviewPanel(admin.ModelAdmin):
    pass

class RestaurantPanel(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdminPanel)
admin.site.register(FoodMenu, FoodMenuPanel)
admin.site.register(Media, MediaPanel)
admin.site.register(Review, ReviewPanel)
admin.site.register(Restaurant, RestaurantPanel)