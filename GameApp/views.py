from urllib import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'GameApp/index.html')

def about(request):
    return render(request, 'GameApp/about.html')

def snake(request):
    return render(request, 'GameApp/snake.html')

def pong(request):
    return render(request, 'GameApp/pong.html')

def ttt(request):
    return render(request, 'GameApp/ttt.html')


