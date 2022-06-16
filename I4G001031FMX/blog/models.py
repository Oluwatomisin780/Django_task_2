from django.db import models
from django.contrib.auth import get_user_model 
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField('%Y-%m-%d %H:%M:%S')
    publish_at = models .DateTimeField('%Y-%m-%d %H:%M:%S')
    author= models.ForeignKey(get_user_model(),on_delete=models.PROTECT)
