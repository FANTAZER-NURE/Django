from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'app1/home.html')


def main(request):
    # return HttpResponse("<h1>aboba2</h1>")
    return render(request, 'app1/index.html')
