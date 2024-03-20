from django.shortcuts import render
from django.http import HttpResponse
from cats.models import Student, Cat

def index(request):
    student_list = Student.objects.order_by('surname')
    cats_list = Cat.objects.all()
    context_dict = {}
    context_dict['title'] = "The students and their cats are:"
    context_dict['students'] = student_list
    context_dict['cats'] = cats_list
    response = render(request, 'cats/index.html', context=context_dict)
    return response

def cats_list(request):
    cats_list = Cat.objects.order_by('name')
    context_dict = {}
    context_dict['title'] = "All the cats are:"
    context_dict['cats'] = cats_list
    response = render(request, 'cats/cats.html', context=context_dict)
    return response
