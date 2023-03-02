from django.shortcuts import render

from.models import Place


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    return render(request,"index.html",{'result':obj})

# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     result = x + y
#     result1 = x - y
#     result2 = x * y
#     result3 = x // y
#     return render(request,"result1.html",{'result':result,'result1':result1,'result2':result2,'result3':result3})
#
