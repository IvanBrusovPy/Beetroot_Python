"""
URL configuration for notes_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from .views import *
urlpatterns = [
    path("index/", index, ),
    path("home/", home_page, name="index"),
    path("add/", add_note_page, name="add"),
    path('edit/<int:note_id>/', edit_note_page, name='edit'),
    path('delete/<int:note_id>/', delete_note, name='delete'),
    path('filter/', filter_note, name='filter'),
    path("search/", search_note, name="search"),
]
