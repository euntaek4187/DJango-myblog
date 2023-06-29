from django.shortcuts import render, redirect
from .models import Blog, Comment
from django.utils import timezone
from django.http import HttpResponseRedirect
import requests
from django.conf import settings


def get_weather_data():
    API_KEY = "0bc87a603c0b8472cbc156c47800a520"
    CITY_NAME = "Seoul"
    API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric"

    response = requests.get(API_URL)
    data = response.json()

    weather_data = {
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure'],
        'wind_speed': data['wind']['speed'],
    }
    return weather_data

def home(request):
    weather_data = get_weather_data()
    context = {
        'blogs': Blog.objects.all(),
        'weather': weather_data
    }
    # blogs = Blog.objects.all()
    return render(request, 'home.html', context)

def detail(request, id):
    blog = Blog.objects.get(id = id)
    return render(request, 'detail.html', { 'blog': blog })

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.image = request.FILES.get('image', None)
    new_blog.document = request.FILES.get('document', None)
    new_blog.pub_date = timezone.now()
    new_blog.save()

    return redirect('detail', new_blog.id)

def edit(request, id):
    edit_blog = Blog.objects.get(id= id)
    return render(request, 'edit.html', {'blog': edit_blog})


def update(request, id):
    update_blog = Blog.objects.get(id= id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    if 'image' in request.FILES:
        update_blog.image = request.FILES['image']
    if 'document' in request.FILES:
        update_blog.document = request.FILES['document']
    update_blog.pub_date = timezone.now()
    update_blog.save()

    return redirect('detail', update_blog.id)


def delete(request, id):
    delete_blog = Blog.objects.get(id= id)
    delete_blog.delete()

    return redirect('home')

def viewMap(req):
    return render(req, 'map.html')

def like_post(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.likes += 1
    blog.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def add_comment(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    text = request.POST['text']
    Comment.objects.create(blog=blog, text=text)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
