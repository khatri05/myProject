from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView
)   
from .forms import CourseForm
# from .forms import StudentForm
from .models import Course, Dept, Student

def home(request):
    #return HttpResponse("Welcome to Django Project!")
    data={
        'name':'Krishna Khatri',
        'course':'Django',
        'collage':'JG-University'
    }
    subject = ['Python-Django', 'Agile', 'Angular', 'BigData']
    return render(request, 'index.html', {'data': data, 'subject_list': subject})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def student(request):
    student_list = [
        'Krishna','Bhavya','Rahul','Rudra','Jay'
    ]
    return render(request, 'student.html', {'students': student_list})

def course1(request):
    course_list = [
        'Python',
        'Django',
        'HTML',
        'CSS',
        'Bootstrap'
    ]
    return render(request, 'course.html', {'courses': course_list})

def grade(request):
    return render(request,'result.html',{'marks':82})

def employee(request):
    emp = [
        {'name':'Krishna','marks':90},
        {'name':'Bhavya','marks':50},
        {'name':'Jash','marks':30}
    ]
    return render(request,'employee.html',{'employees':emp})

def list(request):
    students = Student.objects.all()
    return render(request, 'Student_CRUD/list.html',{'students':students})

# def course(request):
#     return render(request, 'Student_CRUD/course.html')

# def attendance(request):
#     return render(request, 'Student_CRUD/attendance.html')

def add_student(request):

    courses = Course.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        course_id = request.POST.get('course')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        city = request.POST.get('city')

        course = Course.objects.get(id=course_id)

        Student.objects.create(
            name=name,
            course=course,
            email=email,
            mobile=mobile,
            city=city
        )

        return redirect('list')

    return render(request, 'Student_CRUD/add.html', {'courses': courses})

# def add_student(request):
#     if request.method == "POST":
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('list')
#     else:
#         form = StudentForm()
#     return render(request,'Student_CRUD/add.html',{'form':form})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    courses = Course.objects.all()

    if request.method == "POST":
        student.name = request.POST.get('name')
        course_id = request.POST.get('course')
        student.email = request.POST.get('email')
        student.mobile = request.POST.get('mobile')
        student.city = request.POST.get('city')

        course = Course.objects.get(id=course_id)
        student.course = course

        student.save()

        return redirect('list')

    return render(request, 'Student_crud/edit.html', {'student': student, 'courses': courses})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('list')

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'Course_CRUD/course_form.html'
    success_url = reverse_lazy('course_list')
    
class CourseListView(ListView):
    model = Course
    template_name = 'Course_CRUD/course_list.html'
    context_object_name = 'courses'

def dept_details(request):
    depts = Dept.objects.all()
    return render(request, 'Dept_CRUD/dept_details.html', {'depts': depts})