from django.contrib import admin
from .models import Student, Score, Subject

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Score)