from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


class simpleMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return render(request, "login.html")
        #return HttpResponse("Welcome to Middleware")
        #return response