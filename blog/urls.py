from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blogHome"),
    path("blogPosts/<int:id>", views.blogpost, name="blogHome")
]
