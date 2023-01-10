from django.urls import path
from app1.views import *
app_name = 'parent'

urlpatterns = [
    path('parent/',parent,name='parent'),
    path('parent2/',parent2,name='parent2'),
]