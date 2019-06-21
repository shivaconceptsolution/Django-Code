from django.shortcuts import render
from django.http import HttpResponse
from guest.models import Student
def index(request):
	return render(request,"guest/index.html")
	
def addstudent(request):
   s=Student(rno=request.POST["txtrno"],sname=request.POST["txtname"],branch=request.POST["txtbranch"],fees=int(request.POST["txtfees"]))
   s.save()	
   return HttpResponse("data insert successfully")
def viewstudent(request):
  s=Student.objects.all()
  return render(request,"guest/viewstudent.html",{'key':s})
def Editstudent(request):
 s = Student.objects.get(pk=int(request.GET["q"])) 
 return render(request,"guest/editstudent.html",{'key':s})
def Deletestudent(request):
  s = Student.objects.get(pk=int(request.GET["q"]))
  s.delete()
  return HttpResponse("Record Deleted ")    
def si(request):
    p=120000
    r=2.2
    t=2
    s=(p*r*t)/100
    return HttpResponse("Result is "+str(s))	

