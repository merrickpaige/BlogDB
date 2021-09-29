#from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from blog.models import Post, Follower



from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


#from home.forms import HomeForm
from .models import Post, Follower
#from .models import Profile, RequestFriend

def about( request):
        #form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
    
        args = {
             'users': users
        }
        return render(request, "blog/about.html", args)




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


class PostCreateView(LoginRequiredMixin, CreateView):
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
    

def make_followers(request, pk):
    new_follower = User.objects.get(pk=pk)
    
    Follower.make_followers( request.user, new_follower)
    return redirect('/')
    #return redirect('blog:about')

def remove_followers(request, pk):  
    rem_follower = User.objects.get(pk=pk)    
    #if operation == 'remove':
    Follower.remove_followers(request.user, rem_follower)
    return redirect('/')


