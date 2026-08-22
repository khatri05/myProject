from django.urls import path
from . import views
from .views import (
    CourseCreateView,
    CourseListView,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('student', views.student, name='student'),
    path('course', views.course1, name='course'),
    path('result', views.grade, name='result'),
    path('employee', views.employee, name='employee'),
    path('list', views.list, name='list'),
    path('add',views.add_student, name='add'),
    path('edit/<int:id>', views.edit_student, name='edit'),
    path('delete/<int:id>', views.delete_student, name='delete'),
    path('dept_details', views.dept_details, name='dept_details'),
    # CBV for Course CRUD
    path('course_form', CourseCreateView.as_view(), name='course_form'),
    path('course_list', CourseListView.as_view(), name='course_list'),
]