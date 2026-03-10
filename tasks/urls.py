from django.urls import path
from . import views

# from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("thanks", views.thanks_register, name="thanks_register"),
    path("task_list/<int:task_id>", views.task_list, name="task_list"),
    path("add_list", views.add_list, name="add_list"),
    path("edit_list/<int:list_id>", views.edit_list, name="edit_list"),
    path("delete_list/<int:list_id>", views.delete_list, name="delete_list"),
    path("task/<int:task_id>/toggle", views.toggle_task, name="task_toggle"),
    path("add_task/<int:list_id>", views.add_task, name="add_task"),
    path("delete_task/<int:task_id>", views.delete_task, name="delete_task"),
    path("edit_task/<int:task_id>", views.edit_task, name="edit_task"),
]
