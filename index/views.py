from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index/home.html')


def new(request):
    return render(request, 'index/new.html')

