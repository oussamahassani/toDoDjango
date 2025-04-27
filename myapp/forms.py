from unicodedata import name
from venv import create
from django import forms
from .models import Project, Tasks
from django.forms import ModelForm

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Task title", max_length=200, widget=forms.TextInput(attrs={'class':'input'})) 
    description = forms.CharField(label="Task description", widget=forms.Textarea(attrs={'class':'input'}))

    project_id = forms.ModelChoiceField(label="Project", queryset=Project.objects.all())
    important = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    
class CreateNewProject(forms.Form):
    name = forms.CharField(label="Project name", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))

class TaskForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(user=user)
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'project', 'important']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name']




   