from django.contrib import admin
from studentapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['roll_number','name','age','grade']

admin.site.register(Student,StudentAdmin)