from django.shortcuts import render, redirect, get_object_or_404
from .serializers import *
from .forms import *
from .models import *
from rest_framework import viewsets, permissions
from django.views.generic import TemplateView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class IndexView(TemplateView):
    template_name = 'index.html'

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

class EmployeeListView(TemplateView):
    template_name = 'pages/employee_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context

class EmployeeCreateView(TemplateView):
    template_name = 'pages/employee_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EmployeeForm()
        return context

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        return render(request, self.template_name, {'form': form})

class EmployeeUpdateView(TemplateView): 
    template_name = 'pages/employee_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee_id = self.kwargs.get('pk')
        employee = get_object_or_404(Employee, pk=employee_id)
        context['form'] = EmployeeForm(instance=employee)
        return context

    def post(self, request, *args, **kwargs):
        employee_id = self.kwargs.get('pk')
        employee = get_object_or_404(Employee, pk=employee_id)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        return render(request, self.template_name, {'form': form})

class EmployeeDeleteView(TemplateView):
    template_name = 'pages/employee_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee_id = self.kwargs.get('pk')
        context['employee'] = get_object_or_404(Employee, pk=employee_id)
        return context

    def post(self, request, *args, **kwargs):
        employee_id = self.kwargs.get('pk')
        employee = get_object_or_404(Employee, pk=employee_id)
        employee.delete()
        return redirect('employee_list')