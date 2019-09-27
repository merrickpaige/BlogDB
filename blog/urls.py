
from .views import PostListView,PostDetailView, PostCreateView, PostUpdateView,PostDeleteView
from . import views
from django.urls import path

urlpatterns = [
   #path('', views.home, name='blog-home'),
   path('about/', views.about, name='blog-about'),
   path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
   path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
   path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
   path('', PostListView.as_view(), name='blog-home'),
   path('post/new/', PostCreateView.as_view(), name='post-create'),
   
]
