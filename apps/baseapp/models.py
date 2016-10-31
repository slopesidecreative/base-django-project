from django.db import models
from ..loginreg. models import User

# MODEL CONTROLLERS ---------------------------------------------

class ItemManager(models.Manager):
    def register(self,params):
        pass




# BASE MODELS ---------------------------------------------------

class Item(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=200)
    email = models.TextField(max_length=200)
    user = models.ForeignKey(User,related_name='usersitems')
    creator = models.ForeignKey(User,related_name='creator')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = ItemManager()
