from django.shortcuts import render

# Create your views here.

def allclasses(request):
    return render(request, 'products/classes.html')