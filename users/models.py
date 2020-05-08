from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from django.conf import settings
#from django.db import models
from django.db.models.signals import post_save


#added this to the code after
#from django.conf import settings
#from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user = models.OneToOneField(User)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #friends = models.ManyToManyField("Profile", blank=True)

    #userList =User.objects.values()
    # #added this to the code after
    # = models.SlugField()
    #friends = models.ManyToManyField("Profile", blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'
    
def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass

#post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
post_save.connect(post_save_user_model_receiver, sender=User)



class RequestFriend(models.Model):
	user_to = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='to_user_to')
	user_from = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='from_user_from')
	timestamp = models.DateTimeField(auto_now_add=True) # set when created 

	def __str__(self):
		return "From {}, to {}".format(self.user_from.username, self.user_to.username)

     #This tells how we want the profile to be printed in the event we need to proint out the profile.
     #if the User is deleted, delete the profile also.
    #def  save(self,*args, **kwargs):
     #   super().save(*args, **kwargs)

      #  img = Image.open(self.image.path)

       # if img.height > 300 or img.width > 300:
        #    output_size = (300,300)
         #   img.thumbnail(output_size)
           # img.save(self.image.path)

 
# Create your models here.
