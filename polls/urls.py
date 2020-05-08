from polls import views
from django.urls import path
from django.conf.urls import url, include

from polls import views

urlpatterns = [        
    #url(r'^$', views.index, name="index"),
    url('', views.index, name="index"),
]
