from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('employees', views.EmployeeViewSet, basename='employees') # viewsets.viewset
router.register('employee', views.EmployeeModelSet) # viewsets.modelset

urlpatterns = router.urls



# urlpatterns = [
    # path("students", views.StudentView, name="students"), # function-based view
    # path('employee', views.EmployeesViewCls.as_view(), name="EmployeesViewCls"), #class-based views
    # path('employee', views.EmployeeMG.as_view(), name="EmployeeMG"), # mixins + generics
    # path('employee/<int:pk>/', views.EmployeeDetailViewCls.as_view(), name='EmployeeDetailView'),

    # path('employee', views.EmployeeListCreate.as_view()), # generic classes
    # path('employee/<int:pk>', views.EmployeeRUD.as_view())
# ]