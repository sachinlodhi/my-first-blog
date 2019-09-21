from django.shortcuts import render,redirect
# Create your views here.

def post_list(request):
 return  render(request,'blog/post_list.html',{})

