from django.shortcuts import render
from .models import Blog


# Create your views here.
def all_blogs(request):
    """
    A view that gets the latest 5 posts in the
    Blog table, orders them by newest first,
    renders the all_blogs.html template and
    injects the blogs into it
    """
    blogs = Blog.objects.order_by('-pub_date')[:5]

    context = {
        'blogs': blogs
    }

    return render(request, 'all_blogs.html', context)
