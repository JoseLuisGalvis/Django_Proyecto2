from django.shortcuts import render
from .models import Course
# Create your views here.

def about(request):
    courses = Course.objects.all()

    return render(request, 'about/about.html', {'courses':courses})