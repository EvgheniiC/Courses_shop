from django.contrib import admin
from .models import Course, Category

admin.site.site_header = "Courses admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welcome to the courses admin area"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'prise', 'category')


# add table with course in Category seite
class CourserInline(admin.TabularInline):
    model = Course
    exclude = ['created_at']  # without 'created_at' columm
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapce']
        }
        )
    ]
    # add table with course in Category seite
    inlines = [CourserInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
