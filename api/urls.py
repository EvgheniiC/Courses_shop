from api.models import CourseResourse, CategoryResourse
from tastypie.api import Api
from django.urls import path, include


api = Api(api_name="v1")
api.register(CourseResourse()),
api.register(CategoryResourse())

# api/v1/courses/ GET,POST
# api/v1/courses/1/ GET,Delete
# api/v1/categiries/ GET
# api/v1/categiries/1/ GET

urlpatterns = [
    path('', include(api.urls), name='index')
]
