from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts= Post.objects.filter(date_publication__lte=timezone.now()).order_by('date_publication')
    return render(request, 'blog/post_list.html', {'posts1': posts})
