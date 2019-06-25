from django.shortcuts import render,redirect
from django.http import HttpResponse
from customer.models import Register
def index(request):
	return render(request,"customer/index.html")
def login(request):
    u = Register.objects.filter(email=request.POST["txte"])	
    p = Register.objects.filter(password=request.POST["txtp"])	
    flag=True
    res=""
    if(u.count()==0):
     flag=False	
     res= res+"Invalid Emailid "
    if(p.count()==0):
     flag=False	
     res=res+ "Invalid password" 
    if flag:
      request.session["sessemail"]=request.POST["txte"]
      return redirect("/scs/home")
    else:
      return render(request,"customer/index.html",{'key1':res})   


def register(request):
    chk = Register.objects.filter(email=request.POST["txtemail"])
    s=""
    if(chk.count()>0):
        s="Email id Already Exist"
    else:
     r = Register(email=request.POST["txtemail"],password=request.POST["txtpass"],mobile=request.POST["txtmobile"],fullname=request.POST["txtfname"])
     r.save()
     s="Registration successfully"
    return render(request,"customer/index.html",{'key':s})



