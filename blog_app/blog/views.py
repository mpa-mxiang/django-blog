from django.shortcuts import render
from django.http import HttpResponse

post = [
    {
        "author": "Jane Doe",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "09/08/2009"
    },
        {
        "author": "John Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "09/18/2009"
    }
]

def home(request):
    context = {
        'posts': post
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')