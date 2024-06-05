from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=70,  blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    date_modified = models.DateField(User, auto_now=True)
    
    def __str__(self):
        return self.user.username
    
# criando um prifle quando se registra
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        #seguindo o prorpio perfil
        user_profile.follows.set([instance.profile.id])
        user_profile.save()
        
post_save.connect(create_profile, sender=User)

#create a tweet model

class Tweet(models.Model):
    user = models.ForeignKey(User, related_name="tweet", on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return(
            f"{self.user}"
            f"{self.body}..."
            f"({self.create_at: %Y - %m - s%D %H:%M}) "
        )    
    
    