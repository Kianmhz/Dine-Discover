from django.shortcuts import redirect
from django.urls import reverse

class PreventAuthenticatedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        disallowed_urls = [reverse('login'), reverse('signup'), reverse('passR')]

        if request.user.is_authenticated and request.path in disallowed_urls:
            return redirect('home')
        response = self.get_response(request)
        return response
    
class PreventUnAuthenticatedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        disallowed_urls = [reverse('logout'), reverse('profile'), reverse('editP')]

        if not request.user.is_authenticated and request.path in disallowed_urls:
            return redirect('login')
        response = self.get_response(request)
        return response