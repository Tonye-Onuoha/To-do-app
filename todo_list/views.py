from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    todo = Todo.objects.all()
    form = TodoForm()
    context = {"checks":todo,'form':form}
    return render(request,'index.html',context)

@require_POST
def addtodoitem(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

def completed(request,num):
    new = Todo.objects.filter(pk=num)
    obj = new[0]
    obj.completed = True
    obj.save()
    return redirect('index')

def deletecomplete(request):
    for x in Todo.objects.all():
        if x.completed == True:
            x.delete()
    return redirect('index')

def delete_all(request):
    for x in Todo.objects.all():
        x.delete()
    return redirect('index')
