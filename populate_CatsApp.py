import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'CatsApp.settings')

import django
django.setup()
from cats.models import Student, Cat

def populate():
    dannielleCats = [
        {
            'name': 'Khepri',
            'age': 14,
        },
        {
            'name': 'Pandora',
            'age': 8,
        },
        {
            'name': 'Khaleesi',
            'age': 10,
        },
    ]

    taylorCats = [
        {
            'name': 'Meredith Gray',
            'age': 14
        },
        {
            'name': 'Olivia Benson',
            'age': 10
        },
        {
            'name': 'Benjamin Button',
            'age': 6
        },
    ]

    cameronCats = [
        {
            'name': 'Little Man',
            'age': 5
        }
    ]

    mileyCats = [
        {
            'name': 'Lilo',
            'age': 9
        },
        {
            'name': 'Kiki',
            'age': 9
        },
        {
            'name': 'Harlem',
            'age': 8
        }
    ]

    students = {'Dannielle': {'cats': dannielleCats, 'surname': 'Spears',},
            'Taylor': {'cats': taylorCats, 'surname': 'Swift'},
            'Cameron': {'cats': cameronCats, 'surname': 'Diaz'},
            'Miley': {'cats': mileyCats, 'surname': 'Cyrus'}}

    for student, student_data in students.items():
        s = add_student(student, student_data['surname'])
        for cat in student_data['cats']:
            add_cat(cat['name'], cat['age'], s)

    for s in Student.objects.all():
        for c in Cat.objects.filter(owner=s):
            print(f'- {s}: {c}')

def add_student(forename, surname):
    s = Student.objects.get_or_create(forename=forename, surname=surname)[0]
    s.save()
    return s

def add_cat(name, age, owner):
    c = Cat.objects.get_or_create(name=name, owner=owner)[0]
    c.name = name
    c.age = age
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Cat population script...')
    populate()

