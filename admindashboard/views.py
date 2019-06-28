from django.shortcuts import render,redirect
from django.http import HttpResponse
from admindashboard.models import Category,Subcategory
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
def addcat(request):
    c = Category(catname='Furniture')
    c.save()
    return HttpResponse("Category Added Successfully") 
def subcat(request):
     res = Category.objects.all()
     res1 = Subcategory.objects.all()
     if request.method == 'POST':
         if request.POST.get("btncat"):
          c = Subcategory(subcatname=request.POST['txtsubcat'],catid=int(request.POST['ddlcatid']))
          c.save()
     return render(request,"admindashboard/subcat.html",{'key':res,'key1':res1})
def addsubcat(request):
   
    res = Category.objects.all()
    res1 = Subcategory.objects.all()
    return render(request,"admindashboard/subcat.html",{'key':res,'key1':res1})        

