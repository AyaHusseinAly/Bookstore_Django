from django.shortcuts import render,redirect
from django.http import HttpResponseForbidden

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        #return self.get_response(request)
        if request.user.is_active:
            return self.get_response(request)

        return HttpResponseForbidden("you're not active user, contact system administrator for more info")