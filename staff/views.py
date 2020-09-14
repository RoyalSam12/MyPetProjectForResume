from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.views import generic

from .models import Employee
from .forms import EmployeeForm


def index(requests):
    obj = Employee.objects.order_by('-post')
    form = EmployeeForm()
    error = ''

    if requests.method == "POST":
        if requests.POST.get('save') == 'Добавить':
            form = EmployeeForm(requests.POST or None)
            if form.is_valid():
                form.save()
                form = EmployeeForm()
                return HttpResponseRedirect(reverse('mpage:staff:index'))
        elif requests.POST.get('save') == 'Отсортировать':
            try:
                choice = requests.POST['th_choice']
                if choice == 'post':
                    choice = '-' + choice
                    obj = Employee.objects.order_by(choice)
                    form = EmployeeForm()
                else:
                    obj = Employee.objects.order_by(choice)
                    form = EmployeeForm()
            except MultiValueDictKeyError:
                error = 'Выберете по которому ряду желаете отсортировать таблицу'
        elif requests.POST.get('save') == 'Уволить':
            print('gello')

    context = {
        'employee_list': obj,
        'form': form,
        'error_message': error
    }
    return render(requests, 'staff/index.html', context)


'''
def index(requests):
    obj = Employee.objects.order_by('post')
    form = EmployeeForm()
    error = {}
    if form.is_valid():
        form.save()
        form = EmployeeForm()
    if requests.method == 'POST':
        form = EmployeeForm(requests.POST or None)
        if form['first_name']:
            if form.is_valid():
                form.save()
                form = EmployeeForm()
            else:
                try:
                    choice = requests.POST['th_choice']
                    if choice == 'post':
                        choice = '-' + choice
                        obj = Employee.objects.order_by(choice)
                        form = EmployeeForm()
                    else:
                        obj = Employee.objects.order_by(choice)
                        form = EmployeeForm()
                except MultiValueDictKeyError:
                    if form.clean_first_name():
                        error = 'Hello'
                    form = EmployeeForm()
    context = {
        'employee_list': obj,
        'form': form,
        'error_message': error
    }
    return render(requests, 'staff/index.html', context)
'''  # Пробвная попытка вечером


class DetailView(generic.DetailView):
    model = Employee
    template_name = 'staff/detail.html'


def dismiss(requests, pk):
    obj = get_object_or_404(Employee, id=pk)
    if requests.method == 'POST':
        obj.delete()
        return HttpResponseRedirect(reverse('mpage:staff:index'))
    context = {
        'employee': obj,
    }
    return render(requests, 'staff/dismiss.html', context)
