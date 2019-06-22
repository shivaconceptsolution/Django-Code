from django.shortcuts import render,redirect
from django.http import HttpResponse
from guest.models import Student
def index(request):
	return render(request,"guest/index.html")
def loginstudent(request):
  u = Student.objects.filter(rno=request.POST["txtuser"])
  p = Student.objects.filter(sname=request.POST["txtpass"]) 
  res="" 
  flag=True
  if(u.count()==0):
    flag=False
    res=res+"Invalid Username "
  if(p.count()==0):
    flag=False
    res=res+ "Invalid Password"   
  if flag:
    return redirect("viewstudent")
  else:
    return render(request,"guest/index.html",{"key":res})    


def addstudent(request):
   s=Student(rno=request.POST["txtrno"],sname=request.POST["txtname"],branch=request.POST["txtbranch"],fees=int(request.POST["txtfees"]))
   s.save()	
   return redirect("viewstudent")
def viewstudent(request):
  s=Student.objects.all()
  return render(request,"guest/viewstudent.html",{'key':s})
def Editstudent(request):
 s = Student.objects.get(pk=int(request.GET["q"])) 
 return render(request,"guest/editstudent.html",{'key':s})
def updatestudent(request):
 s = Student.objects.get(pk=int(request.POST["txtid"])) 
 s.rno=request.POST["txtrno"]
 s.sname=request.POST["txtname"]
 s.branch=request.POST["txtbranch"]
 s.fees=request.POST["txtfees"]
 s.save()
 return redirect("viewstudent")
def Deletestudent(request):
  s = Student.objects.get(pk=int(request.GET["q"]))
  s.delete()
  return redirect("viewstudent")   
def si(request):
    p=120000
    r=2.2
    t=2
    s=(p*r*t)/100
    return HttpResponse("Result is "+str(s))	

