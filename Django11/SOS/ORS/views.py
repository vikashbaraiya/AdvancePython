from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.sessions.models import Session

from .forms import StudentForm


def hello(request):
    return HttpResponse("<h1> hello..............python<h1>")

def index(request):
    return render(request, "list.html")

def welcome(request):
    return render(request, "list1.html")
def temp(request):
    return render(request, "list3.html")
def index1(request):
    return render(request, "welcome.html", {"firstname":"ram"})

def list(request):
    list = [{"id":1, "name":"vikash"},
            {"id":2, "name":"mohit"},
            {"id":3, "name":"Atharv"},
            {"id":4, "name":"aniket"}]
    return render(request, "list12.html", {'list':list})
def user(request,id=0, name=""):
    massage="User id = " +str(id), " User name = " +str(name)

    return HttpResponse(massage)

def include(request):
    return render(request, "include.html")

def login(request):
    return render(request, "token.html")

def create_Session(request):
    request.session['name'] = 'Admin'
    response = "<h1>Welcome to Session</h1><br>"
    response+= "ID : {0} <br>".format(request.session.session_key)
    return HttpResponse(response)

def access_Session(request):
    response = "Name : {0} <br>".format(request.session.get('name'))
    return HttpResponse(response)

def destroy_Session(request):
    Session.objects.all().delete()
    return HttpResponse("Session is Destroy")

def Add(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("ADD successfully")
    return render(request, "login.html")

def setCookies(request):
    if request.method=="POST":
        name = request.POST.get('cookieName')
        value = request.POST.get('cookieValue')
        res = HttpResponse("<h1>Rays Technologies..</h1>")
        res.set_cookie("name", name)
        res.set_cookie("value", value)
        return res
    return render(request,"SetCookies.html")

def getCookies(request):
    name =request.COOKIES.get('name')
    value = request.COOKIES.get('value')
    html = "<center>Name = {}<br> Value = {}</center>".format(name, value)
    return HttpResponse(html)





