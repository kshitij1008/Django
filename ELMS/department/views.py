from django.shortcuts import render,redirect
from .forms import DepartmentForm
from .models import DepartmentMaster

#Create your views here
def dept(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = DepartmentForm()
    return render(request,'index.html',{'form':form})


def show(request):
    departments = DepartmentForm()
    return render(request,'show.html',{'departments':departments})


def edit(request,id):
    department = DepartmentMaster.object.get(id=id)
    return render(request,'edit.html',{'department':department})


def update(request,id):
    department = DepartmentMaster.object.get(id=id)
    form = DepartmentForm(request.POST,instance=department)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'department': department})


def destroy(request,id):
    department = DepartmentMaster.object.get(id=id)
    department.delete()
    return redirect("/show")
