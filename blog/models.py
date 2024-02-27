from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)
    desc = HTMLField()
    image = models.ImageField(upload_to='blog/category/')
    add_date = models.DateTimeField(auto_now_add=True,null = True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=  100)
    author = models.CharField(max_length=  100,default="")
    slug = models.CharField(max_length=  100)
    desc =  HTMLField()
    timestemp = models.DateField(blank=True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    image = models.ImageField(upload_to = "blog/images",default="")

    def __str__(self):
        return self.title

