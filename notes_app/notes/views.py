from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):  # HttpRequest
    return HttpResponse('Hello from Notes app.')


def index_with_html(request):  # HttpRequest
    return HttpResponse('<h1>Hello from Notes app.</h1>')
