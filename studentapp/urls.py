from django.urls import path
from studentapp import views

urlpatterns = [
    path('student', views.student),
    path('editstudent/<sid>', views.editstudent),
    path('delstudent/<sid>', views.delstudent),   
]
