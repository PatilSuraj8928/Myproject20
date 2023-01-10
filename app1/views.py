from django.shortcuts import render

# Create your views here.
def parent(request):
    return render(request, 'parent.html')

def parent2(request):
    return render(request, 'parent2.html')