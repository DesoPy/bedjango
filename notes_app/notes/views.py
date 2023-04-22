from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()
users = User.objects.all()


def index(request):
    return render(request, 'index.html')


# def index(request):  # HttpRequest
#     return HttpResponse('Hello from Notes app.')


def index_with_html(request, noteshtmlid):  # HttpRequest
    return HttpResponse(f'<h1>Hello from Notes app.</h1><p>{noteshtmlid}</p>')


def page(request):  # HttpRequest
    return HttpResponse('<h3>This is page</h3>')


def tamp(request):
    return render(request, 'sample.html', {
        'name': 'Samwise',
        'ismage': False,
        'items': [
            'salt',
            'rope',
            'ring',
            'lembas',
            'sword'
        ]

    })


def user(request):
    return render(request, 'sample.html', {
        'User': User.objects.all(),
    })


# from django.contrib.auth import get_user_model
#


