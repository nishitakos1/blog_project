from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Contact, Post
from django.contrib import messages


# Create your views here.


def home_view(request):
    return render(request, 'home.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content) 
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<4 :
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "You have successfully submitted your issue !")
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')

def post(request):
    allPosts = Post.objects.all()
    print(allPosts)
    context = {'allPosts' : allPosts}

    return render(request, 'post.html', context)

