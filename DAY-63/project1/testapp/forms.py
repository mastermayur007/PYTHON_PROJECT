from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_name', 'emp_salary', 'emp_department']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['emp_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['emp_salary'].widget.attrs.update({'class': 'form-control'})
        self.fields['emp_department'].widget.attrs.update({'class': 'form-control'})
        self.fields['emp_name'].label = "Employee Name"
        self.fields['emp_salary'].label = "Employee Salary"
        self.fields['emp_department'].label = "Employee Department"
    def clean_emp_salary(self):
        salary = self.cleaned_data.get('emp_salary')
        if salary <= 0:
            raise forms.ValidationError("Salary must be a positive number.")
        return salary
    def clean_emp_department(self):
        department = self.cleaned_data.get('emp_department')
        if not department:
            raise forms.ValidationError("Department is required.")
        return department