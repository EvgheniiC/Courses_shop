from django.urls import path
from . import views

urlpatterns = [
    # first seite
    path('', views.index, name='index'),
    # routing one course seite
    path('<int:course_id>', views.single_course, name='single_course')
]
