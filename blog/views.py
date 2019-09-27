from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

posts = [
    {
    'author':'Merrick Paige ',
    'title':'Blog Post ',
    'content':'First Post ',
    'date_posted':'August 27,2019 '
    },
    {
    'author':'Merrick Paige ',
    'title':'Blog Post ',
    'content':'First Post ',
    'date_posted':'August 27,2019 '
    }
]

#def home(request):
    #context = {
        #'posts': posts
        #'#posts': Post.objects.all()    }
    #return render(request, "blog/about.html", context)
    #return HttpResponse("Hello, world. You're at the polls index.")
    #return HttpResponse(" <h1>Blog Home</h1>")

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = ('/')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    
    
    def test_func(self):
    	post = self.get_object()
    	if self.request.user == post.author:
		    return True
	    #return False

class PostCreateView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
       
        

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = ('/')

    def test_func(self):
    	post = self.get_object()
    	if self.request.user == post.author:
		    return True
	    #return False



def about(request):
    context = {
        'posts': Post.objects.all()}

    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "blog/about.html", context)

# Create your views here.

# Create your views here.
