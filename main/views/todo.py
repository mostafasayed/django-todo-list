from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ..forms import TodoForm
from ..models import Todo


@login_required(login_url='/login')
def index(request):
    user = request.user
    todos = Todo.objects.all().filter(created_by=user)

    context = {
        'todos': todos
    }
    return render(request, 'main/index.html', context)


@login_required(login_url='/login')
def details(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo': todo
    }
    return render(request, 'main/details.html', context)


@login_required(login_url='/login')
def addItem(request):
    user = request.user
    if(request.method == 'POST'):
        form = TodoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = user
            instance.save()

        return redirect('/')
    else:
        addItemForm = TodoForm
        return render(request, 'main/addItem.html', context={"addItem_form": addItemForm})


@login_required(login_url='/login')
def deleteItem(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')


@login_required(login_url='/login')
def updateItem(request, id):
    instance = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'main/addItem.html', context={"addItem_form": form})
