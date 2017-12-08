"""лаба5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from lab import views

urlpatterns = [
    url(r'^base/', views.function_view),
    url(r'^var1/', views.function_view1),
    url(r'^var2/', views.function_view2),
    url(r'^dict/', views.function_view3),
    url(r'^list/', views.function_view4),
    url(r'^books/', views.BooksView.as_view()),
    url(r'^book/(?P<id>\d+)', views.BookView.as_view(), name='book_url'),

]
