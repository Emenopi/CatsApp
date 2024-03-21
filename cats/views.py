from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from cats.models import Student, Cat, Student_Profile
from cats.forms import UserForm, StudentForm, CatForm, StudentProfileForm

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

def show_cat_profile(request, cat_slug):
    context_dict = {}
    try:
        cat = Cat.objects.get(cat_slug=cat_slug)
        context_dict['cat'] = cat
        context_dict['picture'] = cat.picture
    except Cat.DoesNotExist:
        context_dict['picture'] = None
    return render(request, 'cats/cat.html', context=context_dict)

def show_student_profile(request, student_name_slug):
    context_dict = {}
    try:
        student = Student.objects.get(name_slug=student_name_slug)
        cats = Cat.objects.all()
        context_dict['student'] = student
        context_dict['cats'] = cats
    except Student.DoesNotExist:
        context_dict['student'] = None
    return render(request, 'cats/student.html', context=context_dict)

@login_required(login_url='cats:login')
def add_cat(request):
    cat_added = False
    
    if request.method == 'POST':
        cat_form = CatForm(request.POST, request.FILES)
        student_profile = Student_Profile.objects.get(user=request.user)
        owner = student_profile.student
        if cat_form.is_valid():
            cat = cat_form.save(commit=False)
            if 'picture' in request.FILES:
                print("yes")
                cat.picture = request.FILES['picture']
            cat.owner = owner
            cat.save()

            owner.numCats = owner.numCats + 1
            owner.save()
            cat_added = True
        else:
            return HttpResponse(cat_form.errors)
    else:
        cat_form = CatForm()
    return render(request, 'cats/add_cat.html', context={
                                                            'cat_form': cat_form,
                                                            'cat_added': cat_added,
                                                            'user': request.user,
                                                        })


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST)
        profile_form = StudentProfileForm(request.POST)

        if user_form.is_valid() and student_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            student = student_form.save()
            student.save()

            studentProfile = profile_form.save(commit=False)
            studentProfile.user = user
            studentProfile.student = student            
            studentProfile.save()
            registered = True
        else:
            print(user_form.errors, student_form.errors)
    else:
        user_form = UserForm()
        student_form = StudentForm()
        profile_form = StudentProfileForm()

    return render(request, 'cats/register.html', context={
                                                            'user_form': user_form,
                                                            'student_form': student_form,
                                                            'registered': registered
                                                        })

def user_logout(request):
    logout(request)
    return redirect(reverse('cats:index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
            return redirect(reverse('cats:index'))
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details...Try again!")
    else:
        return render(request, 'cats/login.html')
