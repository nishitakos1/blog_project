from django.urls import path
from home import views

urlpatterns = [
    path("",views.home_view, name='Home'),
    path("contact/", views.contact,name='Contact'),
    path("blog/", views.blog,name='Blog'),
    path("post/", views.post ,name='Post'),

    

]
