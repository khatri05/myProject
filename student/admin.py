from django.contrib import admin
from .models import Dept, Student, Course, Attendance
# Register your models here.

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Dept)