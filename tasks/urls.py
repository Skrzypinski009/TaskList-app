from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    # HOME VIEW
    path('', views.index, name='home'),

    # AUTHENTICATION VIEWS
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('thanks', views.thanks_register, name='thanks_register'),

    # ADD VIEWS
    path('add_list', views.add_list, name='add_list'),
    path('add_task/<int:list_id>', views.add_task, name='add_task'),

    # EDIT VIEWS
    path('edit_task/<int:task_id>', views.edit_task, name='edit_task'),
    path('edit_list/<int:list_id>', views.edit_list, name='edit_list'),

    # DELETE VIEWS
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('delete_list/<int:list_id>', views.delete_list, name='delete_list'),
]