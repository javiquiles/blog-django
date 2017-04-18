from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Post

# Vistas con Funciones.
#def post_list(request):
#    posts = Post.objects.all()
#    return render(request, 'blog/post_list.html', {'posts': posts})

#def post_detail(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    return render(request, 'blog/post_detail.html', {'post': post})


#Vistas con Clases.
class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

post_list = PostList.as_view()
post_detail = PostDetail.as_view()
