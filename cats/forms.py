from django import forms
from django.contrib.auth.models import User
from cats.models import Student_Profile, Student, Cat

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('forename', 'surname')

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student_Profile
        fields = ()

class CatForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text='Please enter the cats name: ')
    age = forms.IntegerField(initial=0)

    class Meta:
        model = Cat
        exclude = ('owner', 'cat_slug')