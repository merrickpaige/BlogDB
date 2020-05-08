# Create your models here.
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
#from accounts.models import FProfile,FriendRequest
from users.models import Profile

#REMEMBER Folloer is really the FollowerClass and defining follower is really
# creating folloer is really creating a Follower class for the current user
class Follower(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True)

    @classmethod
    def make_followers(cls, current_user, new_follower):
        follower, created = cls.objects.get_or_create(
            current_user=current_user
        )
        follower.users.add(new_follower)

    @classmethod
    def remove_followers(cls, current_user, rem_follower):
        follower, created = cls.objects.get_or_create(
            current_user=current_user
        )
        follower.users.remove(rem_follower)



class Post(models.Model):
    
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=100)
	#date_posted = models.DateTimeField(date_now_add:True)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    



def get_absolute_url(self):
       return reverse('post-detail', kwargs={'pk': self.pk})
		
def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


def __str__(self):
        return self.title


