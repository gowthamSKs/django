from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .forms import *
from .models import *

# Create your views here.

def index(req):
    return render(req,'index.html')

def home(req):
    return render(req,"home.html")

def con(req):
    
    return render(req,'contact.html')

def base(req):
    return render(req,"base.html")

def table(req):
    context={
        "allproduct":product.objects.all()
    }
    return render(req,"table.html",context)

def register(req):
    con={
        'val':product_form()
    }

    if req.method=="POST":

        prod=product_form(req.POST)
        
        if prod.is_valid():
            prod.save()

       
    return render(req,"register.html",con)

def events(req):
    return render(req,"Events.html")

def deleteuser(req,id):
    userr=product.objects.get(id=id)

    userr.delete()

    return redirect("/table")

def updateuser(req,id):

    userr=product.objects.get(id=id)

    context={
    "val":product_form(instance=userr)
    }
    if req.method=="POST":
        prod=product_form(req.POST,instance=userr)

        if prod.is_valid():
            prod.save()
            return redirect("/table")

    return render(req,'register.html',context)