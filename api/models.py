from django.db import models

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=200,default="no name")
    gender = models.IntegerField(default=0) #0 is men    1 is women    2 is other
    image = models.ImageField(upload_to='api/img/')
    email = models.CharField(max_length=200,default="")
    token = models.CharField(max_length=300)
    fb_token = models.CharField(max_length=200)
    is_active = models.IntegerField(default=0)

    def __str__(self):
     return str(self.email)


class actions(models.Model):
    user1 = models.IntegerField(default=0)
    user2 = models.IntegerField(default=0)
    action = models.IntegerField(default=0) #0 is none / 1 is like / 2 is dislike /3 is block


class main_chat(models.Model):
    user1 = models.IntegerField(default=0)
    user2 = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True,null=True)

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    sender_id = models.IntegerField()
    reciver_id = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=800,blank=True)
 

