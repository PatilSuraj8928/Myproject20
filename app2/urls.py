from django.urls import path
from app2.views import *
app_name = 'child'

urlpatterns = [
    path('child/',child, name = 'child'),
    path('child2/',child2, name='child2'),
    path('child3/',child3, name='child3'),
    path('child4/',child4, name='child4'),
]