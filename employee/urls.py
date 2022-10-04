from unicodedata import name
from django.urls import path
from .views import view_work_time, delete_work_time, add_work_time, view_employee, delete_employee, add_employee

urlpatterns = [
    # view, delete, add work time
    path('view_work_time/', view_work_time, name='view_work_time'),
    path('delete_work_time(?P<int:pid>)/',
         delete_work_time, name='delete_work_time'),
    path('add_work_time/', add_work_time, name='add_work_time'),

    # view employee
    path('view_employee', view_employee, name='view_employee'),
    path('delete_employee(?P<int:pid>)/',
         delete_employee, name='delete_employee'),
    path('add_employee', add_employee, name="add_employee"),
]
