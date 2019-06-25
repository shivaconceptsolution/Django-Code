from django.shortcuts import render,redirect
from django.http import HttpResponse
from customer.models import Register
def index(request):
	if('sessemail' not in request.session):
	  return redirect("/customer")
	res = Register.objects.filter(email=request.session['sessemail'])  
	return render(request,"scs/index.html",{'key':request.session['sessemail'],'key1':res})
def about(request):
	return render(request,"scs/about.html")
def contact(request):
	return render(request,"scs/contact.html")
def gallery(request):
	return render(request,"scs/gallery.html")
def logout(request):
    del  request.session['sessemail']
    return redirect('/customer')		

