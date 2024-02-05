from django.db import models

class Student(models.Model):
    roll_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.roll_number} - {self.name}'