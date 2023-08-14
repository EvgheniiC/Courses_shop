from django.db import models
from django.utils import timezone

# What categories are the courses


class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# course description


class Course(models.Model):
    title = models.CharField(max_length=300)
    prise = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title + ' ' + str(self.students_qty)
