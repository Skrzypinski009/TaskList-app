from django import forms
from .models import Task, TaskList

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, required=True)
    password = forms.CharField(label='Password', max_length=100, required=True, widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', required=True)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, required=True)
    password = forms.CharField(label='Password', max_length=100, required=True, widget=forms.PasswordInput)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']

class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['title']