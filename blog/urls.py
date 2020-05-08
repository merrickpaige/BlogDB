
from .views import PostListView,PostDetailView, PostCreateView, PostUpdateView,PostDeleteView
from . import views
from django.urls import path
from django.conf import settings 

from django.conf.urls.static import static
from django.conf.urls import url

from django.conf.urls import url
#from .views import HomeView
from . import views
from .views import Post, Follower


urlpatterns = [
   #path('', HomeView.as_view(), name='home'),
   #path(' ', views.add_friends, name='add_friends'),
   path('add/<int:pk>/', views.make_followers, name='make_followers'),
   path('remove/<int:pk>/', views.remove_followers, name='remove_followers'), 
    #url(r'^$', HomeView.as_view(), name='home'),
   #path('blog/remove/<int:pk>/', views.remove_friends, name='remove_friends'),


   #path('', views.home, name='blog-home'),
   #path('about/', views.users_list, name='list'),
   path('about/', views.about, name='blog-about'),
   path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
   path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
   path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
   path('', PostListView.as_view(), name='blog-home'),
   path('post/new/', PostCreateView.as_view(), name='post-create'),
   
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 