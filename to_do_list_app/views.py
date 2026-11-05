from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Task
from .forms import TaskForm, TaskEditForm


def home(request):
    """
    Display all tasks on the dashboard table.
    Shows title, description, completion status, created timestamp, and action buttons.
    """
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})


def add_task(request):
    """
    Handle creation of a new task item.
    Accepts title and description from the user.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})


def edit_task(request, pk):
    """
    Handle updating details and completion status of an existing task.
    """
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskEditForm(instance=task)

    return render(request, 'edit_task.html', {'form': form, 'task': task})


def delete_task(request, pk):
    """
    Delete a specific task from the database and redirect to the task list.
    """
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')


def toggle_task(request, pk):
    """
    Toggle task completion status between completed and pending.
    """
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()
    return redirect('home')
