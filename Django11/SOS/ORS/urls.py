
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Hello/', views.hello),
    path('index/', views.index),
    path('vikash/', views.welcome),
    path('mohit/', views.temp),
    path('rohit/', views.index1),
    path('List/', views.list),
    path("User/<int:id>/<str:name>",views.user),
    path("include/", views.include),
    path("token/", views.login),
    path("create/", views.create_Session),
    path("access/", views.access_Session),
    path("destroy/", views.destroy_Session),
    path("add/", views.Add),
    path("set", views.setCookies),
    path("get", views.getCookies),

]
