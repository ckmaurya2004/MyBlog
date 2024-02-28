from django.shortcuts import render
from . models import *

# Create your views here.

def index(request):
    allpost = Post.objects.all()
    cat = Category.objects.all()
    param = {'allpost':allpost,'cat':cat}
    return render(request,'index.html',param)


def about(request,pk,slug):
    post = Post.objects.get(id = pk,slug = slug)
    print(post)
    cat = Category.objects.get(title = post.category)
    print(pk,cat)
 
    return render(request,'about.html',{'cat':cat,'post':post})



def blogPost(request,myid,slug):
    post = Post.objects.filter(id = myid,slug = slug).first()
    cat_post = Category.objects.filter(title = post.category)
    param = {'post':post,'cat_post':cat_post}
    return render(request,'blogpost.html',param)

def category(request,myid):
    cat = Category.objects.all()
    cat1 = Category.objects.get(id = myid)
    allpost = Post.objects.filter(category = cat1)
    param = {'allpost':allpost,'cat':cat}
    return render(request,'index.html',param)



def search(request):
    query = request.POST.get('search')
    if len(query)>50:
        allposts = Post.objects.none()
    else:
        posttitle = Post.objects.filter(title__icontains = query)
        postdesc = Post.objects.filter(desc__icontains = query)
        postauthor = Post.objects.filter(author__icontains = query)
        allposts = posttitle.union(postdesc,postauthor)
    print(allposts)
    param = {'allposts': allposts ,'query':query}       
    return render(request,'search.html',param)
