from django.shortcuts import render
from django.contrib.auth.models import User
from .models import BlogPost
from django.shortcuts import render, get_object_or_404

# Create your views here.


def home_view(request):
    qs = BlogPost.objects.all()
    template_name = 'home.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

def read_article(request, slug):
    obj = get_object_or_404(BlogPost, slug= slug)
    template_name = 'read_article.html'
    context = {'object': obj}
    return render(request, template_name, context)
