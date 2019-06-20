from django.shortcuts import render
from django.http import HttpResponse
from guest.models import Student
def index(request):
	return render(request,"guest/index.html")
	
def addstudent(request):
   s=Student(rno=request.POST["txtrno"],sname=request.POST["txtname"],branch=request.POST["txtbranch"],fees=int(request.POST["txtfees"]))
   s.save()	
   return HttpResponse("data insert successfully")

def si(request):
    p=120000
    r=2.2
    t=2
    s=(p*r*t)/100
    return HttpResponse("Result is "+str(s))	

