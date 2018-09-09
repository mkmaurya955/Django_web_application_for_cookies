from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,'base.html')
def add(request):
    x=int(request.POST['t1'])
    y=int(request.POST['t2'])
    z=x+y
    resp=HttpResponse('value submitted successfully')
    resp.set_cookie('z',z,max_age=30)
    return resp
def display(request):
    if 'z' in request.COOKIES:
        sum=request.COOKIES['z']
        return HttpResponse('addition of two numbers is:'+sum)
    else:
        return HttpResponse('please enter values')