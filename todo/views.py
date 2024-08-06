from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def edit_task(request, pk):
    form = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form.task = request.POST['task']
        form.save()
        return redirect('home')
    
    context = {'form': form }
    return render(request, 'edit_task.html', context)

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')