from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def home(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'home.html', context)

def employee_detials(request, id):
    employee = get_object_or_404(Employee, pk=id)
    print(employee)
    context = {
        "employee": employee
    }
    return render(request, "employee_details.html", context)

@login_required(login_url='login')
@permission_required("employee.add_employee", raise_exception=True)
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})