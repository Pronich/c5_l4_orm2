from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'

    students = Student.objects.all().prefetch_related('teacher').values('id', 'name', 'group', 'teacher__name', 'teacher__subject')

    object_list = []
    student_hash = []
    for student in students:
        if student['id'] not in student_hash:
            student_hash.append(student['id'])
            stud_dict = {}
            stud_dict['id'] = student['id']
            stud_dict['name'] = student['name']
            stud_dict['group'] = student['group']
            stud_dict['teacher'] = [{'name': student['teacher__name'], 'subject': student['teacher__subject']}]
            object_list.append(stud_dict)
        else:
            for obj in object_list:
                if obj['id'] == student['id']:
                    obj['teacher'].append({'name': student['teacher__name'], 'subject': student['teacher__subject']})

    context = {'object_list': object_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
