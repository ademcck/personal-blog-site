from django.shortcuts import render
from django.core.paginator import Paginator
from post.models import Post
from django.db.models import Q

# Create your views here.
def helpers(request, exception):
    return render(request, '404.html')

def home_view(request):
    posts = Post.objects.all() 
    query = request.GET.get('q')
    if query:
        posts = posts.filter(Q(title__icontains=query) | 
                            Q(content__icontains=query)|
                            Q(user__first_name__icontains=query)|
                            Q(user__last_name__icontains=query)).distinct()
    paginator = Paginator(posts, 4) # Show 10 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'home.html',{'posts':page_obj})