from django.shortcuts import render,redirect
from django.http import HttpResponse
def index(request):
	return render(request,"admindashboard/index.html")
def login(request):
    uname=request.POST["txtuser"]
    upass=request.POST["txtpass"]
    if(uname=='admin' and upass=='12345'):
      request.session["aid"]=uname	
      return redirect("dashboard")
    else:
       return HttpResponse("Invalid userid and password")  
def dashboard(request):
   if 'aid' not in request.session:
    return redirect("/adash")	
   else: 
    return render(request,"admindashboard/dashboard.html")        	
def logout(request):
    del request.session["aid"]
    return redirect("/adash")	

