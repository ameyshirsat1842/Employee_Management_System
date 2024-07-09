from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('employee', 'Employee'),
        ('hr', 'HR'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Add this line
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Add this line
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    def __str__(self):
        return self.username


class Employee(models.Model):
    objects = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class LeaveRecord(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('paid', 'Paid Leave'),
        ('sick', 'Sick Leave'),
        ('holiday', 'Holiday'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_records')
    date = models.DateField()
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPE_CHOICES)

    def __str__(self):
        return f'{self.employee} - {self.date} - {self.leave_type}'
