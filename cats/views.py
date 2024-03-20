from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {}
    context_dict['title'] = "The students and their cats are:"
    response = render(request, 'cats/index.html', context=context_dict)
    return response

def cats_list(request):
    context_dict = {}
    context_dict['title'] = "All the cats are:"
    response = render(request, 'cats/cats.html', context=context_dict)
    return response
