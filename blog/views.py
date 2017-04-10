from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, ListView
from .models import Post

# Vistas con Funciones.
#def post_list(request):
#    posts = Post.objects.all()
#    return render(request, 'blog/post_list.html', {'posts': posts})


#Vistas con Clases.
class PostList(ListView):
    model = Post

post_list = PostList.as_view()
