from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return HttpResponse("我是誰")

def about_me(req):
    return render(req,'hello.html')