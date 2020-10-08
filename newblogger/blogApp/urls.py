from django.urls import path
from . import views
from . import admin




urlpatterns = [
    path('', views.index, name='Home'),
    path('contact/',views.contact,name="Contact"),
    path('signup/', views.handelsignup, name="SignUp"),
    path('login/', views.handellogin, name="LogIn"),
    path('logout/', views.handellogout, name='LogOut'),
    path('post/', views.postblog,name="Blog Post"),
    path('search/', views.search, name='Search'),
    path('blog/<str:slug>', views.blogpage, name="BlogPage"),
    path('comment/',views.comment_post, name="Post Comment"),
]
