from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import LoginForm, RegisterForm, TaskForm, TaskListForm
from .models import TaskList, Task


@login_required
def index(request):
    task_lists_data = TaskList.objects.filter(owner=request.user)
    task_lists = [
        {
            "data": x,
            "tasks": Task.objects.filter(task_list=x),
        }
        for x in task_lists_data
    ]

    return render(request, "home.html", {"task_lists": task_lists})


@login_required
def task_list(request, task_id):
    task_list = TaskList.objects.prefetch_related("tasks").get(id=task_id)
    return render(request, "task_list.html", {"task_list": task_list})


@require_POST
def toggle_task(_, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.done = not task.done
        task.save()
        return JsonResponse({"status": "success", "is_done": task.done})
    except Task.DoesNotExist:
        return JsonResponse({"status": "error"}, status=404)


def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    f = RegisterForm()
    if request.POST:
        data = {
            "username": request.POST["username"],
            "password": request.POST["password"],
            "email": request.POST["email"],
        }
        f = RegisterForm(data)
        if f.is_valid():
            # if not User.objects.filter(username=data['username']):
            user = User.objects.create_user(
                username=data["username"],
                password=data["password"],
                email=data["email"],
            )
            user.save()
            return redirect("thanks_register")
    return render(request, "register.html", {"form": f, "title": "Register"})


def thanks_register(request):
    return render(request, "thanks_register.html", {"title": "Thanks!"})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    f = LoginForm()
    if request.POST:
        data = {
            "username": request.POST["username"],
            "password": request.POST["password"],
        }

        f = LoginForm(data)
        if f.is_valid():
            print("valid")
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user is not None:
                print("user authenticated")
                login(request, user)
                return redirect("home")
    return render(request, "login.html", {"form": f, "title": "Login"})


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def add_list(request):
    if request.POST:
        form = TaskListForm(request.POST)
        if form.is_valid():
            other = TaskList.objects.filter(title=request.POST.get("title"))
            if not other:
                task_list = form.save(commit=False)
                task_list.owner = request.user
                task_list.save()
                return redirect("home")
    else:
        form = TaskListForm()
    return render(request, "add_list.html", {"form": form})


def edit_list(request, list_id):
    task_list = TaskList.objects.get(id=list_id)
    if request.POST:
        form = TaskListForm(request.POST, instance=task_list)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskListForm(instance=task_list)
    return render(request, "add_list.html", {"form": form, "list_id": list_id})


@login_required
def add_task(request, list_id):
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            task_list = TaskList.objects.get(id=list_id)
            task = form.save(commit=False)
            task.task_list = task_list
            task.save()
            return redirect("home")
    else:
        form = TaskForm()
    return render(request, "add_task.html", {"form": form, "list_id": list_id})


@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.POST:
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task)
    return render(request, "add_task.html", {"form": form, "task_id": task_id})


@login_required
def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect("home")


@login_required
def delete_list(request, list_id):
    TaskList.objects.get(id=list_id).delete()
    return redirect("home")
