from django.shortcuts import render, redirect
from .models import WorkTime, Employee
from django.contrib import messages
# Create your views here.


# Work time
def view_work_time(request):
    if not request.user.is_active:
        return redirect('index')

    work_times = WorkTime.objects.all()
    context = {
        'work_times': work_times
    }

    return render(request, 'tables-general.html', context)


def delete_work_time(request, pid):
    work_time = WorkTime.objects.get(id=pid)
    work_time.delete()
    return redirect('view_work_time')


def add_work_time(request):
    if not request.user.is_active:
        return redirect('index')

    if request.method == 'POST':
        name = request.POST['name']
        day = request.POST['day']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        start_day = request.POST['start_day']
        end_day = request.POST['end_day']
        time = request.POST['time']

        WorkTime.objects.create(name=name, day=day, start_time=start_time,
                                end_time=end_time, start_day=start_day, end_day=end_day, time=time)
        messages.success(request, 'Tạo thành công!')
    return render(request, 'forms-elements.html')


# Employee
def view_employee(request):
    if not request.user.is_active:
        return redirect('index')

    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'view-employee.html', context)


def delete_employee(request, pid):
    employee = Employee.objects.get(id=pid)
    employee.delete()
    return redirect('view_employee')


def add_employee(request):
    if not request.user.is_active:
        return redirect('index')

    employees = Employee.objects.values('gender').distinct()
    work_times = WorkTime.objects.values('id', 'name').distinct()

    context = {
        'employees': employees,
        'work_times': work_times
    }

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        work_time = request.POST['work_time']

        Employee.objects.create(
            name=name, age=age, gender=gender, email=email, phone=phone, work_time_id=work_time)
        messages.success(request, 'Tạo thành công')

    return render(request, 'add-employee.html', context)
