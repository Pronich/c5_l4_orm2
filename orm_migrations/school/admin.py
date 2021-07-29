from django.contrib import admin

from .models import Student, Teacher

# class RelatedInline(admin.TabularInline):
#     model = Student.teacher.through
#     extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # inlines = [
    #     RelatedInline,
    # ]
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # inlines = [
    #     RelatedInline,
    # ]
    # exclude = ('student',)
    pass
