from django import template
from cats.models import Student


register = template.Library()

@register.inclusion_tag('cats/students.html')
def get_student_list():
    return {'students': Student.objects.all()}