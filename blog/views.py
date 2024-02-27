from django.shortcuts import render
from . models import *

# Create your views here.

def index(request):
    allpost = Post.objects.all()
    cat = Category.objects.all()
    param = {'allpost':allpost,'cat':cat}
    return render(request,'index.html',param)


def blogPost(request,slug,myid):
    post = Post.objects.filter(id = myid,slug = slug).first()
    cat_post = Category.objects.filter(title = post.category)
    param = {'post':post,'cat_post':cat_post}
    return render(request,'blogpost.html',param)

def about(request):
    return render(request,'about.html')


def category(request,myid):
    cat = Category.objects.all()
    cat1 = Category.objects.get(id = myid)
    allpost = Post.objects.filter(category = cat1)
    param = {'allpost':allpost,'cat':cat}
    return render(request,'index.html',param)



def search(request):
    print(request)
    query = request.GET.get('search','')
    print(query)
    if len(query)>50:
        allpost = Post.objects.none()
    else:
        posttitle = Post.objects.filter(title__icontains = query)
        postdesc = Post.objects.filter(desc__icontains = query)
        postauthor = Post.objects.filter(author__icontains = query)
        allposts = posttitle.union(postdesc,postauthor)
    cat = Category.objects.all()
    param = {'allposts': allposts ,'query':query,'cat':cat}       
    return render(request,'index.html',param)
