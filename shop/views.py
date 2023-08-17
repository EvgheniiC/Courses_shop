from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Course, Category


def index(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def single_course(request, course_id):
    # option 1
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, 'single_course.html', {'course': course})
    # except Course.DoesNotExist:
    #     raise Http404

    # option 2
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'single_course.html', {'course': course})
