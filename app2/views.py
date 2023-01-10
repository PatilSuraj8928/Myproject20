from django.shortcuts import render

# Create your views here.
def child(request):
    return render(request, 'child.html')

def child2(request):
    return render(request, 'child2.html')

def child3(request):
    return render(request, 'child3.html')

def child4(request):
    return render(request, 'child4.html')