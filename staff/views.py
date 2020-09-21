from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

from .models import Employee
from .forms import EmployeeForm, DetailForm


def detail(requests, pk):
    form = DetailForm
    employee = Employee.objects.get(id=pk)
    if requests.method == 'POST':
        employee.detail_set.update(
            detail_text=requests.POST['detail_text'],
            address=requests.POST['address'],
            e_mail=requests.POST['e_mail'],
            employee=pk
        )
    template_name = 'staff/detail.html'
    context = {
        'form': form,
        'employee': employee
    }
    return render(requests, template_name, context)


def add_info(requests, pk):
    form = DetailForm()
    employee = Employee.objects.get(id=pk)
    if requests.method == "POST":
        employee.detail_set.create(
            detail_text=requests.POST['detail_text'],
            address=requests.POST['address'],
            e_mail=requests.POST['e_mail'],
            employee=pk
        )
        return HttpResponseRedirect(reverse('mpage:staff:detail', args=[pk]))
    context = {
        'employee_inf': pk,
        'form': form
    }
    return render(requests, 'staff/add_info.html', context)


def index(requests):
    obj = Employee.objects.order_by('-salary')
    form = EmployeeForm()
    error = ''

    if requests.method == "POST":
        if requests.POST.get('save') == 'Добавить':
            form = EmployeeForm(requests.POST or None)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('mpage:staff:index'))
        elif requests.POST.get('save') == 'Отсортировать':
            try:
                choice = requests.POST['th_choice']
                if choice == 'post':
                    choice = '-' + choice
                    obj = Employee.objects.order_by(choice)
                    form = EmployeeForm()
                elif choice == 'salary':
                    choice = '-' + choice
                    obj = Employee.objects.order_by(choice)
                    form = EmployeeForm()
                else:
                    obj = Employee.objects.order_by(choice)
                    form = EmployeeForm()
            except MultiValueDictKeyError:
                error = 'Выберете по которому ряду желаете отсортировать таблицу'

    context = {
        'employee_list': obj,
        'form': form,
        'error_message': error
    }
    return render(requests, 'staff/index.html', context)


def dismiss(requests, pk):
    obj = get_object_or_404(Employee, id=pk)
    if requests.method == 'POST':
        obj.delete()
        return HttpResponseRedirect(reverse('mpage:staff:index'))
    context = {
        'employee': obj,
    }
    return render(requests, 'staff/dismiss.html', context)
