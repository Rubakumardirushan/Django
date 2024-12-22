from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
from django.urls import reverse

def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")

def create(request):
    return HttpResponse("Hello, world. You're at the blog create.")

def show(request, blog_id):
    return HttpResponse(f"Hello, world. You're at the blog show {blog_id}.")

def oldredirect(request):
    return redirect(reverse('newredirect'))

def newredirect(request):
    return HttpResponse("Hello, world. You're at the blog newredirect.")