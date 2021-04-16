from django.shortcuts import render

# Create your views here.
def sample1(request):
    return render(request,"sample1.html")

def sample2(request,data):
    return render(request,"myapp/sample2.html",context={'data':data})

def sample3(request):
    return render(request,"myapp/sample3.html",context={'name':"vishnu"})