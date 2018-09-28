from django.shortcuts import render
from .models import Posts
# Create your views here.
def index(request):
    posts = Posts.objects.all()
    return render(request,'index.html',{'posts':posts,})

def full_pic(request,pic_id):
    posts = Posts.objects.filter(id=pic_id)
    return render(request,'one.html',{'posts':posts})

def dcmarv(request,category_id):
    posts = Posts.objects.filter(category_id=category_id)
    return render(request,'dcmarv.html',{'posts':posts})
