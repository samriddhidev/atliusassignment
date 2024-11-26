from django.shortcuts import render,redirect
from .models import Task
from django.contrib.auth.decorators import login_required
@login_required
def task_list(request):
    tasks=Task.objects.filter(user=request.user)
    return render(request,'tasks/tasks_list.html', {'tasks':tasks})

@login_required
def task_create(request):
    if request.method=='POST':
        title=request.POST['title']
        description= request.POST['description']
        Task.object.create(title=title,description=description,user=request.user)
        return redirect('task_list')
    return render(request,'tasks/task_create.html')
    

# Create your views here.
