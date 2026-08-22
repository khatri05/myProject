from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20,unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    faculty_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.course_name} - {self.course_code}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True,blank=True)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    remarks = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.student.name} - {self.date}"

class Dept(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_code = models.CharField(max_length=20,unique=True)
    supervisor_name = models.CharField(max_length=100)
    dept_type = models.CharField(max_length=50)
    hod_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.dept_name} - {self.dept_code}"