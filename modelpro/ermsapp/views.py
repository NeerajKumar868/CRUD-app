from django.shortcuts import redirect, render
from .models import Employee
from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    emplist = Employee.objects.all()
    return render(request,"ermsapp/index.html",{'emplist':emplist})

def save(request):
    if request.method == "GET":
        return render(request,'ermsapp/form.html',{'action':'Save'})
    elif request.method =="POST":
        EmpID = request.POST['empId']
        EmpName = request.POST['empName']
        EmpSalary = request.POST['empSalary']
        EmpTeam = request.POST['empTeam']
        emp_obj = Employee.objects.create(EmpID=EmpID,EmpName=EmpName,EmpSalary=EmpSalary,EmpTeam=EmpTeam)
        emp_obj.save()
        return redirect('/ermsapp/home')
    emplist= Employee.objects.all()#select * ermsapp_Employees
    return render(request,'ermsapp/index.html',{'emplist':emplist})


def delete(request,empID):
    emp_obj=Employee.objects.get(EmpID=empID)
    emp_obj.delete()
    return redirect('/ermsapp/home')

def deleteAll(request):
    emp_obj=Employee.objects.all()
    emp_obj.delete()
    return redirect("/ermsapp/home")


def Edit(request,empID):
    emp_obj=Employee.objects.get(EmpID=empID)
    return render(request,'ermsapp/form.html',{'action':'Update','emp_obj':emp_obj})

def update(request):
    if request.method=="POST":
        EmpID = request.POST['empId']
        EmpName = request.POST['empName']
        EmpSalary = request.POST['empSalary']
        EmpTeam = request.POST['empTeam']
        emp = Employee.objects.filter(EmpID=EmpID)
        emp.update(EmpName=EmpName,EmpSalary=EmpSalary,EmpTeam=EmpTeam)
        return redirect("/ermsapp/home")

def sortname(request):
    emplist = Employee.objects.order_by('EmpID')
    return render(request,'ermsapp/index.html',{'emplist':emplist})




def searchname(request):
    query=request.GET['search']
    emplist=Employee.objects.filter("EmpName_endswith=query")
    return render(request,'ermsapp/index.html',{'emplist':emplist})
    