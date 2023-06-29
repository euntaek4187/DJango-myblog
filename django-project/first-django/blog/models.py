from django.db import models
import time

# Create your models here.
# class Blog(models.Model):
#     title = models.CharField(max_length=200)
#     writer = models.CharField(max_length=100)
#     pub_date = models.DateTimeField()
#     body = models.TextField()

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()