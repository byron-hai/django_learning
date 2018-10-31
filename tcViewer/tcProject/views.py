from django.shortcuts import render, redirect
# Create your views here.


def demo(request):
    return render(request, 'general_test.html', {'msg': 'hhhaha'})

