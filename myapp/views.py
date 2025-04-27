from django.db import IntegrityError
from .models import Project, Tasks
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject, TaskForm, ProjectForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def index(request):
    title = 'Django Project'
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    username = 'khouloud lazreg'
    return render(request, 'about.html', {
        'username': username
    })

@login_required
def project(request):
    project = Project.objects.filter(user=request.user)
    return render(request, 'projects/projects.html', {
        'project': project
    })

@login_required
def tasks(request):
    task = Tasks.objects.filter(usersesion=request.user).order_by('-datecompleted')
    project = Project.objects.filter(user=request.user)
    areas = ['All','Completed','Pending']
    return render(request, 'tasks/tasks.html', {
        'task': task,
        'projects': project,
        'areas':areas
    })

@login_required
def createtask(request):
    if request.method == 'GET':
        form = TaskForm(request.user)
        return render(request, 'tasks/create_task.html', {
            'form': form
        })

    else:   
        try:
            form = TaskForm(request.user, request.POST)
            if form.is_valid():
                new_task = form.save(commit=False)
                new_task.usersesion = request.user
                new_task.save()
                return redirect('tasks')
        except ValueError:
            return render(request, 'tasks/create_task.html', {
            'form': TaskForm,
            'error': "Please provide valid data"
        })

@login_required
def createproject(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'formproject': ProjectForm
        })
    else:
        # Project.objects.create(name=request.POST['name'], user=request.user)
        try:
            form = ProjectForm(request.POST)
            new_project = form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            return redirect('projects')
        except ValueError:
            return render(request, 'projects/create_project.html', {
            'formproject': ProjectForm,
            'error': 'Please provide valid data'
        })

@login_required
def projectdetail(request, id):
    project = get_object_or_404(Project, id=id, user=request.user)
    tasks = Tasks.objects.filter(project_id=id)
    return render(request, 'projects/details.html', {
        'project': project,
        'tasks': tasks
    })

@login_required
def projectdelete(request, id):
    project = get_object_or_404(Project, id=id, user=request.user)
    tasks = Tasks.objects.filter(project_id=id)
    return render(request, 'projects/project_delete.html', {
        'project_id': project,
        'tasks': tasks
    })

@login_required
def projectdeleteconfirm(request, id):
    project = get_object_or_404(Project, id=id, user=request.user)
    project.delete()
    return redirect('projects')

@login_required
def deletetask(request, id):
    task = get_object_or_404(Tasks, id=id, usersesion=request.user)
    task.delete()
    return redirect('tasks')

@login_required
def donetask(request, id):
    task = get_object_or_404(Tasks, id=id, usersesion=request.user)
    task.done = True
    task.datecompleted = timezone.now()
    task.save()
    return redirect('tasks')

@login_required
def taskdetail(request, id):
    if request.method == 'GET':
        task = get_object_or_404(Tasks, id=id, usersesion=request.user)
        form = TaskForm(request.user, instance=task)
        return render(request, 'tasks/task_detail.html',{
            'task': task,
            'form': form
        })
    else:
        try:
            task = get_object_or_404(Tasks, id=id, usersesion=request.user)
            form = TaskForm(request.user, request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'tasks/task_detail.html',{
            'task': task,
            'form': form,
            'error': "Error updating task"
        })

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup/signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'signup/signup.html', {
                    'form': UserCreationForm,
                    'error': "User already exist"
                })
        return render(request, 'signup/signup.html', {
                    'form': UserCreationForm,
                    'error': "Password doesn't match"
                })

def log(request):
    if request.method=='GET':
        return render(request, 'signup/login.html',{
        'form': AuthenticationForm
    })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user == None:
            return render(request, 'signup/login.html',{
                'form': AuthenticationForm,
                'error': "User or password incorrect"
            })
        else:
            login(request, user)
            return redirect('index')

@login_required
def signout(request):
    logout(request)
    return redirect('login')

