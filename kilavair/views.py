from django.http import Http404
from django.shortcuts import render

def home_page(request):
    return render(request, 'index.html')


def header(request):
    return render(request, 'shared/Header.html')


def footer(request):
    return render(request, 'shared/footer.html')

def about(request):
    return render(request, 'about-us.html')


def engineering(request):
    return render(request, 'service/engineering.html')


