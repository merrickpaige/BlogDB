from django.conf.urls import url

from .views import (
	users_list, )

urlpatterns = [
    url(r'^$', users_list, name='list'),    
    ]