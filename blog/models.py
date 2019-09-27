# Create your models here.
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=100)
	#date_posted = models.DateTimeField(date_now_add:True)
	date_posted = models.DateTimeField(default=timezone.now)
    #author = models.ForeignKey(User, unique=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)


def get_absolute_url(self):
       return reverse('post-detail', kwargs={'pk': self.pk})
		
def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})





def __str__(self):
        return self.title


