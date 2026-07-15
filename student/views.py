from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def home(request):
    #return HttpResponse("Welcome to Django Project!")
    data={
        'name':'Krishna Khatri',
        'course':'WDP-Django',
        'collage':'JG-Univerity'
    }
    subject = ['Python-Django', 'Agile', 'Angular', 'BigData']
    return render(request, 'index.html', {'data': data, 'subject_list': subject,'marks':80})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')