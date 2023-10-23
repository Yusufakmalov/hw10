from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def home_page(request):
#     return HttpResponse('<h1>Hello<h1/>')

def index_page(request):
    return render(request, 'news.html')
def about_page(request):
    return render(request, 'login.html')