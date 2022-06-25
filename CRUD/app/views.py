from django.shortcuts import redirect, render
from .models import Employees

# Create your views here.
def INDEX(request):
    
    emp = Employees.objects.all()
    
    return render(request,'index.html',{'emp':emp})


def ADD(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        Employees(name=name,email=email,phone=phone,address=address).save()
        return redirect('/')
        
    # return render(request,'index.html')


def EDIT(request):
    emp = Employees.objects.all()
    
    return redirect(request,'/',{'emp':emp})

def Update(request,id):
    if request.method == "POST":
   
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
    
        emp = Employees.objects.filter(id = id).update(name=name,email=email,phone=phone,address=address)
        return redirect('/')
        
    return redirect(request,'index.html')

