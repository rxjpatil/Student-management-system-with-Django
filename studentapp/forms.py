from django import forms
from studentapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_number','name','age','grade']

    # def __init__(self, *args, **kwargs):
    #     super(EmployeeForm, self).__init__(*args, **kwargs)

    #     # Set the size attribute for the text input fields
    #     self.fields['emp_id'].widget.attrs['size'] = 5
    #     self.fields['hiring_date'].widget.attrs['size'] = 5
    #     self.fields['salary'].widget.attrs['size'] = 5