from django.shortcuts import render, get_object_or_404
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


def detail(request, blog_id):
    """
    A view that displays the details of a particular
    blog that matches the blog_id
    """
    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog
    }

    return render(request, 'detail.html', context)
