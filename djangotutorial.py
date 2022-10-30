#pip install django
#django-admin startproject DemoProject
#cd DemoProject
#python manage.py runserver (manage.py will help connect to server)
#An address will be returned
#python manage.py startapp DemoApp
#under DemoApp, under migrations we have views.py
#in views.py, from django.http import HttpResponse
#create a func
#       def hi(response):
             #return HttpResponse("<h1>Heading</h1>")
#
#create urls.py under migrations
#open urls.py in demoproject.py
#scroll down and copy the 'from django.urls import path, include..... till end'
#paste it in urls.py present in web app directory
#write 'from . import views.py'
#in url patterns in the same file, in path('', views.hi, name='home-page'),
#
#in urls.py in demoproject, under urlpatterns, path('', include(DemoApp.urls))
#

