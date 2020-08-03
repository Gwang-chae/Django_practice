"""my_polls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name = 'index'),      #현재 경로 http://localhost:8000/polls
    path('<int:page_num1>/', views.detail, name ='detail'),
    path('<int:page_num2>/vote/', views.vote, name ='vote')
]
