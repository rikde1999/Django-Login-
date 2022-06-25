from django.shortcuts import redirect, render
from .models import Info
# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['text']
        
        db = Info(name=name,email=email,comment=comment)
        db.save()
    return render(request, 'home.html')

def data(request):
    data = Info.objects.all()
    return render(request, 'data.html',{'data':data})

def delete_data(request,id):
    Info.objects.filter(Id = id).delete()
    return redirect('/data')


def update_page(request,id):
    upd = Info.objects.filter(Id = id)
    return render(request,'update.html',{'data' : upd})


def update(request):
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['text']
        upd = Info.objects.filter(Id = id).update(name=name,email=email,comment=comment)
    
    return redirect('/data')


    