from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, LeaveRecord
from .forms import CustomUserCreationForm, EmployeeForm, LeaveRecordForm


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    leave_records = employee.leave_records.all()
    return render(request, 'employee_detail.html', {'employee': employee, 'leave_records': leave_records})


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})


def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})


def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})


def leave_record_create(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        form = LeaveRecordForm(request.POST)
        if form.is_valid():
            leave_record = form.save(commit=False)
            leave_record.employee = employee
            leave_record.save()
            return redirect('employee_detail', pk=employee_id)
    else:
        form = LeaveRecordForm()
    return render(request, 'leave_record_form.html', {'form': form, 'employee': employee})


def leave_record_update(request, employee_id, record_id):
    leave_record = get_object_or_404(LeaveRecord, pk=record_id, employee_id=employee_id)
    if request.method == 'POST':
        form = LeaveRecordForm(request.POST, instance=leave_record)
        if form.is_valid():
            form.save()
            return redirect('employee_detail', pk=employee_id)
    else:
        form = LeaveRecordForm(instance=leave_record)
    return render(request, 'leave_record_form.html', {'form': form, 'employee': leave_record.employee})


def leave_record_delete(request, employee_id, record_id):
    leave_record = get_object_or_404(LeaveRecord, pk=record_id, employee_id=employee_id)
    if request.method == 'POST':
        leave_record.delete()
        return redirect('employee_detail', pk=employee_id)
    return render(request, 'leave_record_confirm_delete.html', {'leave_record': leave_record})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


