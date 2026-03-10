from django.urls import path
from . import views

# from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="home"),
    # AUTH
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("thanks", views.thanks_register, name="thanks_register"),
    # TASK LIST
    path("task_list/<int:task_id>", views.task_list, name="task_list"),
    path("task_list/add", views.add_list, name="add_list"),
    path("task_list/<int:list_id>/edit", views.edit_list, name="edit_list"),
    path("task_list/<int:list_id>/delete", views.delete_list, name="delete_list"),
    path("tasklist/<int:list_id>/add_task", views.add_task, name="add_task"),
    # TASK
    path("task/<int:task_id>/toggle", views.toggle_task, name="task_toggle"),
    path("task/<int:task_id>/delete", views.delete_task, name="delete_task"),
    path("task/<int:task_id>/edit", views.edit_task, name="edit_task"),
]
