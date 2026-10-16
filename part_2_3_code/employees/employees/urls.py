from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.employee_detials, name='employee_name'),
    path('add', views.add_employee, name="add_employee")
]