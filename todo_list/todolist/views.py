from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo

def todo_list(request):
  todos = Todo.objects.filter(user=request.user)
  return render(request, 'todolist.html', {'todos': todo_list(todos)})

def todo_create(request):
  if request.method == 'POST':
    form = TodoForm(request.POST)
    if form.is_valid():
      todo = form.save(commit=False)
      todo.user = request.user
      todo.save()
      return redirect('todo_list')
    else:
      form = TodoForm()
    return render(request, 'todo_create.html', {'form': form})
  
def todo_update(request, pk):
  todo = get_object_or_404(Todo, pk=pk, user=request.user)
  if request.method== 'POST':
    form = TodoForm(request.POST, instance=todo)
    if form.is_valid():
      todo = form.save(commit=False)
      todo.user = request.user
      todo.save()
      return redirect('todo_list')
    else:
      form = TodoForm(instance=todo)
    return render(request, 'todo_update.html', {'form': form})
  
def todo_delete(request, pk):
  todo = get_object_or_404(Todo, pk=pk, user=request.user)
  todo.delete()
  return redirect('todo_list')
