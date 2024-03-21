from django.contrib import admin
from cats.models import Student, Cat, Student_Profile


class StudentAdmin(admin.ModelAdmin):
    list_display = ('forename', 'surname', 'numCats')

class CatAdmin(admin.ModelAdmin):
    list_display= ('name', 'age', 'owner')

admin.site.register(Student, StudentAdmin)
admin.site.register(Cat, CatAdmin)
admin.site.register(Student_Profile)