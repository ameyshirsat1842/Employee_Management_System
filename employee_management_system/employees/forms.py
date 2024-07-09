from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Employee, LeaveRecord


class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('employee', 'Employee'),
        ('hr', 'HR'),
    ]
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'position', 'salary', 'hire_date']


class LeaveRecordForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = LeaveRecord
        fields = ['date', 'leave_type']
