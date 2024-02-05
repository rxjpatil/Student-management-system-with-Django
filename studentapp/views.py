from django.shortcuts import render,redirect
from studentapp.models import Student
from studentapp.forms import StudentForm

def student(request):
    e=Student.objects.all()
    context={}
    if request.method == 'POST':
        form = StudentForm(request.POST)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect('/student')
    context['data']=e
    return render(request,'student.html',context)

def editstudent(request,sid):
    e = Student.objects.filter(roll_number=sid)
    if not e.exists():
        return redirect('/student')

    employee = e.first()

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/student')
    else:
        form = StudentForm(instance=employee)

    context = {'form': form}
    return render(request, 'editstudent.html', context)

def delstudent(request,sid):
    c=Student.objects.filter(roll_number=sid)
    c.delete()
    return redirect('/student')